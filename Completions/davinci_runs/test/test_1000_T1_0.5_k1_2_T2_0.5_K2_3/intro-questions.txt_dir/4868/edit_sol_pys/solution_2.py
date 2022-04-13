#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'



def main():
    white_pieces = input('Белые фигуры: ').split(',')
    white_pieces = [piece[0].upper() + piece[1:] for piece in white_pieces]
    black_pieces = input('Черные фигуры: ').split(',')
    black_pieces = [piece[0].lower() + piece[1:] for piece in black_pieces]
    board = [list('........') for _ in range(8)]
    for piece in white_pieces:
        board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = piece[0]
    for piece in black_pieces:
        board[int(piece[1]) - 1][ord(piece[0]) - ord('a')] = piece[0]
    print('+---+---+---+---+---+---+---+---+')
    for row in board:
        print('|' + '|'.join(['.' + piece + '.' if piece != '.' else ':::' for piece in row]) + '|')
        print('+---+---+---+---+---+---+---+---+')


if __name__ == '__main__':
    main()
