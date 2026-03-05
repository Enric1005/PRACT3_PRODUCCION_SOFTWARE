class DomainError(Exception):
    """Error base del dominio"""

    pass


class EmptyTitleError(DomainError):
    """Error con el titulo"""

    pass


class InvalidAmountError(DomainError):
    """Error con la cantidad"""

    pass


class InvalidExpenseDateError(DomainError):
    """Error con la fecha de expedición"""

    pass
