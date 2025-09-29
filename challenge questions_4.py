#This program finds and prints all the prime numbers within the given range.
#For this code i took help from AI tool, cause i couldn't figure out exactly where should i start from.

def find_primes_in_range(start,end):
    """

    Args:
    start (int): The starting number of the range.
    end (int): The ending number of the range.
    """
    print(f"Prime numbers in the range from{start} to {end}:")

    for num in range(start, end +1):
        if num>1:
            is_prime = True
            for i in range(2, int(num**0.5) + 1):

                if (num % i) ==0:
                    is_prime = False
                    break
            if is_prime:
                print(num, end= " ")
    print("\n")

start_range = 10
end_range = 100
find_primes_in_range(start_range, end_range)
