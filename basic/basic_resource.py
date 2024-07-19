from log.btkg_logger import BtkgLogger


class BasicResource:
    __logger: BtkgLogger = None

    @property
    def logger(self) -> BtkgLogger:
        return self.__logger

    @logger.setter
    def logger(self, logger: BtkgLogger):
        self.__logger = logger

    def __compose_debug_msg(self, msg: str) -> str:
        return type(self).__name__ + msg

    def debug(self, msg: str):
        self.__logger.debug(self.__compose_debug_msg(msg))

    def debug_verbose(self, msg: str):
        self.logger.debug(self.__compose_debug_msg(msg), True)

    def info(self, msg: str):
        self.__logger.info(self.__compose_debug_msg(msg))

    def error(self, msg: str):
        self.__logger.error(self.__compose_debug_msg(msg))
