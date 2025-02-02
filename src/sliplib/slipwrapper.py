#  Copyright (c) 2020. Ruud de Jong
#  This file is part of the SlipLib project which is released under the MIT license.
#  See https://github.com/rhjdjong/SlipLib for details.

"""
Module :mod:`~sliplib.slipwrapper`
==================================

The :mod:`~sliplib.slipwrapper` module contains the abstract base class :class:`SlipWrapper`
that is the basis for concrete implementations that combine the SLIP protocol with a byte stream.

The :class:`SlipWrapper` class can also be imported directly from the :mod:`sliplib` package.

.. autotypevar:: ByteStream
   :no-type:

.. autoclass:: SlipWrapper
   :show-inheritance:

   Class :class:`SlipWrapper` offers the following methods and attributes:

   .. automethod:: recv_msg
   .. automethod:: send_msg
   .. autoattribute:: driver
   .. autoattribute:: stream

   In addition, :class:`SlipWrapper` requires that derived classes implement the following methods:

   .. automethod:: recv_bytes
   .. automethod:: send_bytes

"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from collections.abc import Iterator

from sliplib.slip import Driver

ByteStream = TypeVar("ByteStream")  #: :class:`ByteStream` represents a generic byte stream.


class SlipWrapper(abc.ABC, Generic[ByteStream]):
    """Abstract base class that provides a message based interface to a byte stream.

    :class:`SlipWrapper` combines a :class:`~sliplib.slip.Driver` instance with a (generic) byte stream.
    The :class:`SlipWrapper` class is an abstract base class.
    It offers the methods :meth:`send_msg` and :meth:`recv_msg` to send and
    receive single messages over the byte stream, but it does not of itself
    provide the means to interact with the stream.

    To interact with a concrete stream, a derived class must implement
    the methods :meth:`send_bytes` and :meth:`recv_bytes`
    to write to and read from the stream.

    A :class:`SlipWrapper` instance can be iterated over.
    Each iteration will provide the next message that is received from the byte stream.

    .. versionchanged:: 0.5
       Allow iteration over a :class:`SlipWrapper` instance.
    """

    def __init__(self, stream: ByteStream):
        """
        To instantiate a :class:`SlipWrapper`, the user must provide
        an existing byte stream.

        Args:
            stream (:class:`ByteStream`): The byte stream that will be wrapped.
        """
        #: The wrapped :class:`ByteStream`.
        self.stream = stream
        #: The :class:`SlipWrapper`'s :class:`~sliplib.slip.Driver` instance.
        self.driver = Driver()

    @abc.abstractmethod
    def send_bytes(self, packet: bytes) -> None:
        """Send a packet over the stream.

        Derived classes must implement this method.

        Args:
            packet: the packet to send over the stream
        """

    @abc.abstractmethod
    def recv_bytes(self) -> bytes:
        """Receive data from the stream.

        Derived classes must implement this method.

        .. note::
            The convention used within the :class:`SlipWrapper` class
            is that :meth:`recv_bytes` returns an empty bytes object :obj:`b""`
            to indicate that the end of
            the byte stream has been reached and no further data will follow.
            Derived implementations must ensure that
            this convention is followed.

        Returns:
            The bytes received from the stream
        """

    def send_msg(self, message: bytes) -> None:
        """Send a SLIP-encoded message over the stream.

        Args:
            message: The message to encode and send
        """
        packet = self.driver.send(message)
        self.send_bytes(packet)

    def recv_msg(self) -> bytes:
        """Receive a single message from the stream.

        Returns:
            A SLIP-decoded message

        Raises:
            ProtocolError: when a SLIP protocol error has been encountered.
                A subsequent call to :meth:`recv_msg` (after handling the exception)
                will return the message from the next packet.
        """
        while (message := self.driver.get(block=False)) is None:
            data = self.recv_bytes()
            self.driver.receive(data)
        return message

    def __iter__(self) -> Iterator[bytes]:
        while True:
            if not (msg := self.recv_msg()):
                break
            yield msg
