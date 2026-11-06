#!/usr/bin/env python3
"""
drive_index_generator.py — Auto-index Google Drive folders for AP Cybersecurity

Generates a markdown index of all files in configured qsec_* folders.
Run after each upload batch to keep index current.

Usage:
    python3 drive_index_generator.py --creds /path/to/school_token.pickle --output /path/to/index.md
"""

import argparse
import os
import pickle
from datetime import datetime
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

# ──────────────────────────────────────────────────────────────────────────
# FOLDER CONFIGURATION — REPLACE PLACEHOLDERS IMMEDIATELY AFTER FOLDER CREATION
# Format: "Folder Name": "FOLDER_ID_HERE"
# ──────────────────────────────────────────────────────────────────────────
FOLDERS = {
    "qsec_u3": "1LZMBjm0DfqCJy14vhB0W4jsSefh5DTjV",
    "qsec_u4": "1vM7BbQ5KPs22KCnTHEnNPrQvJiHGlhBd",
    "qsec_u5": "1d8L42XRfcxeXbippsLc6OpiSvL3myT-h",
    "qsec_u6": "1lhLN-57zdQFN5f_AAjccd_ZJM80uz2ss",
    "qsec_practice": "1_jSfqDu2adP47LvRiR1Sh-WD8WCfTsNd",
    "qsec_capstone": "1aA2po49YapLJmorF_x8G1wyN3aPLH2fs",
    "qsec_ap_review": "1HB8JiJsG019-A5f8vIAT2IpEzybfuYU8",
}

# Subfolders to traverse (relative to each root folder)
SUBFOLDERS = {
    "qsec_u3": ["Worksheets", "Answer Keys"],
    "qsec_u5": ["lessons", "worksheets", "quizzes", "keys"],
    "qsec_practice": [],
    "qsec_capstone": [],
    "qsec_ap_review": [],
    "qsec_u6": ["lessons", "supporting"],
}


def load_creds(pickle_path: str):
    with open(pickle_path, "rb") as f:
        creds = pickle.load(f)
    if not creds.valid:
        creds.refresh(Request())
    return creds


def list_folder(drv, folder_id: str, prefix: str = ""):
    """Recursively list all files in a folder, returning (name, id, mimeType, path)."""
    results = []
    page_token = None
    while True:
        resp = drv.files().list(
            q=f"'{folder_id}' in parents and trashed=false",
            fields="nextPageToken, files(id, name, mimeType)",
            pageToken=page_token,
            pageSize=1000,
        ).execute()
        for f in resp.get("files", []):
            full_path = f"{prefix}/{f['name']}" if prefix else f["name"]
            results.append((f["name"], f["id"], f["mimeType"], full_path))
            if f["mimeType"] == "application/vnd.google-apps.folder":
                results.extend(list_folder(drv, f["id"], full_path))
        page_token = resp.get("nextPageToken")
        if not page_token:
            break
    return results


def format_size(size_str: str) -> str:
    """Convert bytes to human-readable."""
    try:
        b = int(size_str)
        for unit in ["B", "KB", "MB", "GB"]:
            if b < 1024:
                return f"{b:.1f} {unit}"
            b /= 1024
        return f"{b:.1f} TB"
    except:
        return ""


def generate_index(drv, output_path: str):
    lines = []
    lines.append("# AP Cybersecurity — Google Drive Index")
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")
    lines.append("")
    lines.append("| Folder | File | Type | Drive ID |")
    lines.append("|--------|------|------|----------|")

    total_files = 0
    for folder_name, folder_id in FOLDERS.items():
        if folder_id == "FOLDER_ID_HERE":
            lines.append(f"| {folder_name} | *Folder ID not configured* | — | — |")
            continue

        try:
            files = list_folder(drv, folder_id, folder_name)
            if not files:
                lines.append(f"| {folder_name} | *(empty)* | — | — |")
            for name, fid, mime, path in files:
                if mime == "application/vnd.google-apps.folder":
                    ftype = "Folder"
                elif mime.startswith("application/vnd.google-apps."):
                    ftype = "GDoc"
                elif mime == "text/markdown":
                    ftype = "Markdown"
                elif mime == "application/pdf":
                    ftype = "PDF"
                else:
                    ftype = mime.split("/")[-1].upper()
                lines.append(f"| {folder_name} | {path} | {ftype} | {fid} |")
            total_files += len(files)
        except Exception as e:
            lines.append(f"| {folder_name} | *Error: {e}* | — | — |")

    lines.append("")
    lines.append(f"**Total entries:** {total_files}")
    lines.append(f"**Folders configured:** {len(FOLDERS)}")
    lines.append("")
    lines.append("---")
    lines.append("*Run `python3 drive_index_generator.py --creds ~/.hermes/school_token.pickle --output index.md` to regenerate.*")

    with open(output_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Index written to {output_path} ({total_files} entries)")


def main():
    parser = argparse.ArgumentParser(description="Generate Drive index for AP Cybersecurity folders")
    parser.add_argument("--creds", required=True, help="Path to school_token.pickle")
    parser.add_argument("--output", required=True, help="Output markdown file path")
    args = parser.parse_args()

    creds = load_creds(args.creds)
    drv = build("drive", "v3", credentials=creds)
    generate_index(drv, args.output)


if __name__ == "__main__":
    main()