from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")

    # Input secret integers from Party1 and Party2
    secret_a = SecretInteger(Input(name="A", party=party1))
    secret_b = SecretInteger(Input(name="B", party=party2))

    # Compute the result of adding the two secret integers
    result = secret_a + secret_b

    # Output the result to Party3
    output = Output(result, "sum_result", party3)

    return [output]

# Example usage
outputs = nada_main()
for output in outputs:
    print(output)
