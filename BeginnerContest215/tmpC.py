from math import factorial


def main():
    tmp = input().split()
    S = sorted(list(tmp[0]))
    K = int(tmp[1])
    K = K - 1  # 処理が0 = 1番目、1 = 2番目とn-1=n番目に対応しているので1を引く
    num_list = list(range(len(S)))  # [0,1,2,3,4,5,6,7,8,9]を作成
    factorical_list = [factorial(i) for i in range(len(num_list))]  # 階乗のリストを作成 factorical_list = [0,1!,2!,3!,4!,5!,6!,7!,8!,9!]
    print(num_list)
    print(factorical_list)
    ans = '' #答え用の変数
    for f in reversed(factorical_list):  # 階乗のリストを逆順にfへ代入
        ans += S[num_list.pop(K // f)]  # nをfで割った商のindexにある数字をansの後ろに付け加える
        K = K % f  # n/fの余りを新たなnとする
    print(ans)


if __name__ == '__main__':
    main()
