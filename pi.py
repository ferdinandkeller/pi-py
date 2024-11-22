"""Approximate the value of PI using the Archimedes algorithm."""

from decimal import Decimal, getcontext

from loguru import logger


def main() -> None:
    """Start the algorithm."""
    logger.info("Let's compute pi!")

    number_of_iterations = 1020

    hyp = Decimal(2)

    for _ in range(number_of_iterations):
        hyp = step(hyp)

    logger.success("Current best approximation of pi")
    logger.success(approx_pi(hyp, number_of_iterations))


def approx_pi(hyp_n: Decimal, n: int) -> Decimal:
    """
    Approximate the value of PI from the nth iteration of the hypothenuse.

    :param hyp_n: hypothenuse at the nth iteration
    :param n: iteration number
    :return: approximate value of PI
    """
    return 2**n * hyp_n


def step(hyp_n: Decimal) -> Decimal:
    """
    Step the hypothenuse to the next iteration.

    :param hyp_n: hypothenuse at the nth iteration
    :return: hypothenuse at the n+1 iteration
    """
    half_hyp_n_sqr = (hyp_n / 2) ** 2
    i_n = (1 - half_hyp_n_sqr).sqrt()
    j_n = 1 - i_n
    return (half_hyp_n_sqr + j_n**2).sqrt()


if __name__ == "__main__":
    getcontext().prec = 100  # n-1 digits after the decimal point
    main()
