import argparse
from modules.recon import run_recon
from modules.scan import run_scan

def main():
    parser = argparse.ArgumentParser(description="ALL IN ONE Hacking Tool For Hackers")
    parser.add_argument("--recon", help="Run reconnaissance", action="store_true")
    parser.add_argument("--scan", help="Run scanning", action="store_true")
    args = parser.parse_args()

    if args.recon:
        run_recon()
    elif args.scan:
        run_scan()
    else:
        print("No option selected. Use --help for usage.")

if __name__ == "__main__":
    main()
