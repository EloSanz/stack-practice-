from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.db import Base

class AddressDB(Base):
    __tablename__ = "addresses"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    street_name: Mapped[str] = mapped_column(String, nullable=False)
    street_number: Mapped[int] = mapped_column(nullable=False)
    lat: Mapped[int] = mapped_column(nullable=False)
    long: Mapped[int] = mapped_column(nullable=False)

    persons: Mapped[list["PersonDB"]] = relationship("PersonDB", back_populates="address")

class PersonDB(Base):
    __tablename__ = "persons"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first: Mapped[str] = mapped_column(String, nullable=False)
    lastname: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    address_id: Mapped[int] = mapped_column(ForeignKey("addresses.id"), nullable=False)

    address: Mapped["AddressDB"] = relationship("AddressDB", back_populates="persons")
