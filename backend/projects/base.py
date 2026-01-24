# backend/projects/base.py

from abc import ABC, abstractmethod
from typing import List, Type
from pydantic import BaseModel

class BaseProject(ABC):
    """
    Base class for all projects.
    Each project is a configuration that defines
    how an agent should be built.
    """

    @property
    @abstractmethod
    def project_id(self) -> str:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        pass

    @property
    @abstractmethod
    def tools(self) -> List:
        pass

    @property
    @abstractmethod
    def response_schema(self) -> Type[BaseModel]:
        pass
