"""Possui variáveis globais do jogo

Attributes:
    DEFAULT_CHIPS (int): quantidade padrão de fichas iniciais
    playing (bool): loop principal do jogo
    RANKS (tuple): ranking das cartas do baralho
    SUITS (tuple): naipe das cartas do jogo
    SUITS_UNICODE (dict): converte naipe em código unicode
    VALUES (dict): converte ranking das cartas em valor no jogo
"""
import random

#GLOBAL VARIABLES 
SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
SUITS_UNICODE = {"Hearts":"\u2661","Diamonds":"\u2662","Spades":"\u2660","Clubs":"\u2663"}
RANKS = ("two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace")
VALUES = {"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"jack":10,"queen":10,"king":10,"ace":11}

DEFAULT_CHIPS = 1000

playing = True
