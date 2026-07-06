from arguments import get_args

def main():
    args = get_args()

    if args.verbose and args.bank_nr is None:
        print("No bank number provided.")
    if args.verbose and args.job_nr is None:
        print("No job number provided.")

    print(f"Bank Number: {args.bank_nr}")
    print(f"Job Number: {args.job_nr}")


if __name__ == "__main__":
    main()