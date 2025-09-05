from rsa import RSA  # Import the RSA class from rsa.py
import sys

def load_input_file(file_path):
    """Loads and parses the input.txt file to extract prime numbers and messages."""
    with open(file_path, 'r') as f:
        content = f.readlines()

    test_cases = []
    
    # Iterate through content by checking for primes and collecting following lines as messages
    i = 0
    while i < len(content):
        prime_line = content[i].strip()
        
        # Check if the line contains prime numbers
        if prime_line:
            try:
                # First line contains primes p and q
                p, q = map(int, prime_line.split())

                # Initialize an empty list to store messages
                messages = []
                
                # Collect the next 5 lines as messages
                for j in range(1, 6):  # Expecting 5 message lines
                    if i + j < len(content):
                        message_line = content[i + j].strip()
                        if message_line:
                            messages.append(int(message_line))
                
                # Append the prime numbers and messages to test_cases
                test_cases.append((p, q, messages))
                
                # Move the index past the message lines
                i += 6  # 1 for the primes, 5 for the messages

            except ValueError as e:
                print(f"Error parsing line {i+1}: {e}")
                i += 1
        else:
            i += 1

    return test_cases


def execute_rsa_operations(test_cases):
    """Executes RSA encryption and decryption for each test case."""
    results = []

    for p, q, messages in test_cases:
        rsa = RSA()
        rsa.compute_key(p, q, 3)  # Using the coprime index 3 as an example

        # For each message, encrypt and then decrypt it
        for msg in messages:
            encrypted_msg = rsa.encrypt(msg)
            decrypted_msg = rsa.decrypt(encrypted_msg)
            # Store results as a tuple
            results.append((p, q, rsa.phi, (rsa.n, rsa.e), (rsa.n, rsa.d), msg, encrypted_msg, decrypted_msg))

    return results


if __name__ == "__main__":
    # Command line arguments validation
    if len(sys.argv) != 3 or sys.argv[1] != '-i':
        print("Usage: python test.py -i input.txt")
        sys.exit(1)

    # Input file path is the second argument
    input_file_path = sys.argv[2]

    # Load and process input from the file
    test_cases = load_input_file(input_file_path)

    # Run RSA operations (encryption/decryption)
    results = execute_rsa_operations(test_cases)

    # Output results in a formatted way
    for result in results:
        p, q, phi, pu, pr, message, encrypted, decrypted = result
        print(f"p: {p}, q: {q}, phi: {phi}, pu: {pu}, pr: {pr}, "
              f"message: {message}, encrypted: {encrypted}, decrypted: {decrypted}")
