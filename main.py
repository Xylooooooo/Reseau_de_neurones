from squelette import *


def test_init_classique():
    nb_x = 3
    nb_h = 4
    nb_y = 2
    params = initialisation_classique(nb_x, nb_h, nb_y)
    print("W1 =", params["W1"])
    print("b1 =", params["b1"])
    print("W2 =", params["W2"])
    print("b2 =", params["b2"])


def main():
    test_init_classique()

if __name__ == "__main__":
    main()
