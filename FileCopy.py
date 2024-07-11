def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            for line in src:
                dest.write(line)
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = 'source.txt'
destination_file = 'destination.txt'

copy_file(source_file, destination_file)