import argparse
from .vision import VisionMode


def watch_text(target: str, timeout: float):
    print(f"👁️ Watching for text: '{target}'")
    print("Press CTRL+C to stop\n")

    vision = VisionMode(verbose=True)
    state = vision.wait_text(target, timeout=timeout)

    if state.detected:
        print(f"\n✅ Texto '{target}' detectado!")
    else:
        print(f"\n❌ Texto '{target}' NÃO detectado.")

    print("\n--- Diagnostics ---")
    print(f"Attempts: {state.attempts}")
    print(f"Elapsed: {state.elapsed:.2f}s")
    print(f"Confidence: {state.confidence:.2f}")


def watch_icon(icon_path: str, timeout: float):
    print(f"👁️ Watching for icon: '{icon_path}'")
    print("Press CTRL+C to stop\n")

    vision = VisionMode(verbose=True)
    state = vision.wait_icon(icon_path, timeout=timeout)

    if state.detected:
        print(f"\n✅ Ícone '{icon_path}' detectado!")
    else:
        print(f"\n❌ Ícone '{icon_path}' NÃO detectado.")

    print("\n--- Diagnostics ---")
    print(f"Attempts: {state.attempts}")
    print(f"Elapsed: {state.elapsed:.2f}s")
    print(f"Confidence: {state.confidence:.2f}")


def main():
    parser = argparse.ArgumentParser(
        prog="nano-vision",
        description="👁️ Visual automation CLI (nano-wait-vision)"
    )

    subparsers = parser.add_subparsers(dest="command")

    # 🔍 watch-text
    text_parser = subparsers.add_parser("watch-text", help="Wait for text on screen")
    text_parser.add_argument("target", type=str)
    text_parser.add_argument("--timeout", type=float, default=10)

    # 🖼️ watch-icon
    icon_parser = subparsers.add_parser("watch-icon", help="Wait for icon on screen")
    icon_parser.add_argument("path", type=str)
    icon_parser.add_argument("--timeout", type=float, default=10)

    # 🔥 comando viral (auto detecta)
    watch_parser = subparsers.add_parser("watch", help="Wait for text OR icon")
    watch_parser.add_argument("target", type=str)
    watch_parser.add_argument("--timeout", type=float, default=10)

    args = parser.parse_args()

    if args.command == "watch-text":
        watch_text(args.target, args.timeout)

    elif args.command == "watch-icon":
        watch_icon(args.path, args.timeout)

    elif args.command == "watch":
        if args.target.endswith(".png"):
            watch_icon(args.target, args.timeout)
        else:
            watch_text(args.target, args.timeout)

    else:
        parser.print_help()