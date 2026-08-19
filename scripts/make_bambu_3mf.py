#!/usr/bin/env python3
"""
Convenience helper: convert one or more STLs into a multi-object 3MF
suitable for Bambu Studio.

Usage:
    python3 make_bambu_3mf.py part1.stl part2.stl --out project.3mf

Notes:
- For CadQuery parts with internal cavities, prefer exporting 3MF
  directly from CadQuery instead of going through STL.
- This script uses trimesh and is safe only for solid meshes.
"""

import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser(description="STLs → multi-object 3MF for Bambu")
    parser.add_argument("stls", nargs="+", help="Input STL files")
    parser.add_argument("--out", default="bambu_project.3mf", help="Output 3MF path")
    args = parser.parse_args()

    try:
        import trimesh
    except ImportError:
        print("trimesh is required", file=sys.stderr)
        sys.exit(1)

    scene = trimesh.Scene()
    for path in args.stls:
        if not os.path.isfile(path):
            print(f"Missing file: {path}", file=sys.stderr)
            sys.exit(1)
        mesh = trimesh.load(path, force="mesh")
        name = os.path.splitext(os.path.basename(path))[0]
        scene.add_geometry(mesh, geom_name=name)

    scene.export(args.out)
    print(f"Wrote {args.out} with {len(args.stls)} object(s)")

if __name__ == "__main__":
    main()
