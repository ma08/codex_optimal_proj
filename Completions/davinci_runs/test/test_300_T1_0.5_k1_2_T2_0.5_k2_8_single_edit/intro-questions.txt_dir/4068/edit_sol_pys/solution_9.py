#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
from scipy import linalg



def main():
    N, K = map(int, input().split())
    A = np.array([int(input()) for _ in range(N)])
    B = np.array([int(input()) for _ in range(N)])
    C = np.array([int(input()) for _ in range(N)])
    D = np.array([int(input()) for _ in range(N)])
    E = np.array([int(input()) for _ in range(N)])
    F = np.array([int(input()) for _ in range(N)])
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(E)
    # print(F)
    A_sum = np.sum(A)
    B_sum = np.sum(B)
    C_sum = np.sum(C)
    D_sum = np.sum(D)
    E_sum = np.sum(E)
    F_sum = np.sum(F)
    # print(A_sum)
    # print(B_sum)
    # print(C_sum)
    # print(D_sum)
    # print(E_sum)
    # print(F_sum)
    A_ave = A_sum / N
    B_ave = B_sum / N
    C_ave = C_sum / N
    D_ave = D_sum / N
    E_ave = E_sum / N
    F_ave = F_sum / N
    # print(A_ave)
    # print(B_ave)
    # print(C_ave)
    # print(D_ave)
    # print(E_ave)
    # print(F_ave)
    A_var = np.var(A, ddof=1)
    B_var = np.var(B, ddof=1)
    C_var = np.var(C, ddof=1)
    D_var = np.var(D, ddof=1)
    E_var = np.var(E, ddof=1)
    F_var = np.var(F, ddof=1)
    # print(A_var)
    # print(B_var)
    # print(C_var)
    # print(D_var)
    # print(E_var)
    # print(F_var)
    cov_AB = np.cov(A, B, ddof=1)[0][1]
    cov_AC = np.cov(A, C, ddof=1)[0][1]
    cov_AD = np.cov(A, D, ddof=1)[0][1]
    cov_AE = np.cov(A, E, ddof=1)[0][1]
    cov_AF = np.cov(A, F, ddof=1)[0][1]
    cov_BC = np.cov(B, C, ddof=1)[0][1]
    cov_BD = np.cov(B, D, ddof=1)[0][1]
    cov_BE = np.cov(B, E, ddof=1)[0][1]
    cov_BF = np.cov(B, F, ddof=1)[0][1]
    cov_CD = np.cov(C, D, ddof=1)[0][1]
    cov_CE = np.cov(C, E, ddof=1)[0][1]
    cov_CF = np.cov(C, F, ddof=1)[0][1]
    cov_DE = np.cov(D, E, ddof=1)[0][1]
    cov_DF = np.cov(D, F, ddof=1)[0][1]
    cov_EF = np.cov(E, F, ddof=1)[0][1]
    # print(cov_AB)
    # print(cov_AC)
    # print(cov_AD)
    # print(cov_AE)
    # print(cov_AF)
    # print(cov_BC)
    # print(cov_BD)
    # print(cov_BE)
    # print(cov_BF)
    # print(cov_CD)
    # print(cov_CE)
    # print(cov_CF)
    # print(cov_DE)
    # print(cov_DF)
    # print(cov_EF)
    cov_matrix = np.array([[A_var, cov_AB, cov_AC, cov_AD, cov_AE, cov_AF],
                           [cov_AB, B_var, cov_BC, cov_BD, cov_BE, cov_BF],
                           [cov_AC, cov_BC, C_var, cov_CD, cov_CE, cov_CF],
                           [cov_AD, cov_BD, cov_CD, D_var, cov_DE, cov_DF],
                           [cov_AE, cov_BE, cov_CE, cov_DE, E_var, cov_EF],
                           [cov_AF, cov_BF, cov_CF, cov_DF, cov_EF, F_var]])
    # print(cov_matrix)
    eig_val, eig_vec = linalg.eig(cov_matrix)
    # print(eig_val)
    # print(eig_vec)
    eig_val_index = np.argsort(eig_val)[::-1]
    # print(eig_val_index)
    eig_vec_index = eig_vec[:, eig_val_index]
    # print(eig_vec_index)
    eig_vec_index_K = eig_vec_index[:, :K]
    # print(eig_vec_index_K)
    eig_vec_index_K_T = eig_vec_index_K.T
    # print(eig_vec_index_K_T)
    print(eig_vec_index_K_T.dot(np.array([A_ave, B_ave, C_ave, D_ave, E_ave, F_ave])))
    # print(eig_vec_index_K_T.dot(np.array([A_ave, B_ave, C_ave, D_ave, E_ave, F_ave])))


if __name__ == "__main__":
    main()
