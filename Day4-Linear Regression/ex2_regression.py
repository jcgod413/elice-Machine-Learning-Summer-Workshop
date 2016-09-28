import io
import numpy
import statsmodels.api
import elice_utils


def main():
    (N, X, Y) = read_data()
    results = do_simple_regression(N, X, Y)

    elice_utils.visualize(X, Y, results)

def read_data():
    # 1
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

def do_simple_regression(N, X, Y):
    # 2
    X = numpy.array(X).T
    X = statsmodels.api.add_constant(X)
    results = statsmodels.api.OLS(Y, X).fit()

    return results

if __name__ == "__main__":
    main()
