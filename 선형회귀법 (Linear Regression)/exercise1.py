import numpy

def main():
    (N, X, Y) = read_data()
    print(N)
    print(X)
    print(Y)

def read_data():
    # Implement here
    N = int(input().strip()) # receive first line
    X = []
    Y = []

    for i in range(N):
        line = input().strip() # receive each line
        line_splitted = line.split(" ")
        X.append(float(line_splitted[0]))
        Y.append(float(line_splitted[1]))

    return (N, X, Y)

if __name__ == "__main__":
    main()
