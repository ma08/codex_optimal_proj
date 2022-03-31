
from collections import defaultdict

N, M = map(int, input().split())

# 各電球に影響を与えるスイッチのidを格納する辞書
# key: bulb_id
# value: [switch_id1, switch_id2, ...]
bulb_id_to_switch_ids = defaultdict(list)

for bulb_id in range(1, M + 1):
    switch_ids = list(map(int, input().split()))
    bulb_id_to_switch_ids[bulb_id] = switch_ids[1:]

# 各電球のon/off状態
# key: bulb_id
# value: on/off
bulb_id_to_state = {}
for bulb_id in range(1, M + 1):
    state = int(input())
    bulb_id_to_state[bulb_id] = state

# 各スイッチに影響を受ける電球のidを格納する辞書
# key: switch_id
# value: [bulb_id1, bulb_id2, ...]
switch_id_to_bulb_ids = defaultdict(list)

for bulb_id, switch_ids in bulb_id_to_switch_ids.items():
    for switch_id in switch_ids:
        switch_id_to_bulb_ids[switch_id].append(bulb_id)

# 全てのスイッチの状態を格納する辞書
# key: switch_id
# value: on/off
switch_id_to_state = {}
for switch_id in range(1, N + 1):
    # 全てのスイッチは最初はoffにしておく
    switch_id_to_state[switch_id] = 'off'

# 全てのスイッチの状態を探索する
# 全てのスイッチの状態は、
# on: 0
# off: 1
# として扱う
# 全てのスイッチの状態を表現する数値は、0から2^N - 1までの値を取る
for switch_state_num in range(2 ** N):
    # 各スイッチの状態を決める
    for switch_id in range(1, N + 1):
        # switch_idのビットが1かどうかを調べる
        if switch_state_num & (1 << switch_id - 1):
            switch_id_to_state[switch_id] = 'off'
        else:
            switch_id_to_state[switch_id] = 'on'

    # 全ての電球を点灯させることができるかを調べるループ
    # 全ての電球が点灯している場合は、次のスイッチの状態を調べる
    # 点灯していない電球がある場合は、このスイッチの状態はダメなので、次のスイッチの状態を調べる
    for bulb_id in range(1, M + 1):
        bulb_state = bulb_id_to_state[bulb_id]
        switch_ids = bulb_id_to_switch_ids[bulb_id]
        on_switch_num = 0
        for switch_id in switch_ids:
            switch_state = switch_id_to_state[switch_id]
            if switch_state == 'on':
                on_switch_num += 1

        if bulb_state == 0 and on_switch_num % 2 != 0:
            break
        elif bulb_state == 1 and on_switch_num % 2 != 0:
            break
    else:
        # 全ての電球が点灯している場合
        # 全てのスイッチの状態を表示するループ
        print('switch_state_num:', switch_state_num)
        for switch_id in range(1, N + 1):
            print(switch_id, switch_id_to_state[switch_id])
        print()
