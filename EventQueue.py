#!/usr/bin/env python3

import queue
from abc import abstractmethod
from enum import Enum


class Event(Enum):
    Event_None = 0
    Event_DashBoard = 1
    Event_Recenter = 2
    Event_PowerDown = 3


class MyQueue(object):
    def __init__(self):
        self.__queue = queue.Queue()

    def isFull(self):
        return self.__queue.full()

    def isEmpty(self):
        return self.__queue.empty()

    def enqueue(self, data):
        self.__queue.put(data)

    def dequeue(self):
        return self.__queue.get()

    def getSize(self):
        return self.__queue.qsize()

    def clean(self):
        data = 0
        while self.__queue.qsize() != 0:
            self.__queue.get(data)


class EventHub(object):
    __static_instance = {}
    def __init__(self):
        self.__dict__ = EventHub.__static_instance
        self.__queue = MyQueue()
        self.__handler = []

    def add_handler(self, handler):
        self.__handler.append(handler)

    def attach(self, event):
        self.__queue.enqueue(event)

    def notify(self):
        event = self.__queue.dequeue()
        for handler in self.__handler:
            handler.event_handler(event)


class EventHandler(object):
    @abstractmethod
    def event_handler(self, event):
        pass


class RecenterEvent(EventHandler):
    def event_handler(self, event):
        if event == Event.Event_Recenter:
            print("this is recenter event handler.")


class PowerDownEvent(EventHandler):
    def event_handler(self, event):
        if event == Event.Event_PowerDown:
            print("this is power down event handler.")


class DashboardEvent(EventHandler):
    def event_handler(self, event):
        if event == Event.Event_DashBoard:
            print("this is dashboard event handler")


def main():
    event_hub = EventHub()
    event_hub.add_handler(RecenterEvent())
    event_hub.add_handler(PowerDownEvent())
    event_hub.add_handler(DashboardEvent())

    event_hub.attach(Event.Event_DashBoard)
    event_hub.attach(Event.Event_PowerDown)
    event_hub.notify()
    event_hub.notify()


if __name__ == "__main__":
    main()
