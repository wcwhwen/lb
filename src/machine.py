from src.fsm import TocMachine # import trick

# 此段代碼要和 fsm.py 中的 class TocMachine 定義的函式還有畫出來的 FSM 圖搭配看
# transitions 是一個 list of dictionaries
# 其中，dictionary 中的 "trigger" key 可以設定成: "advance" 和 "go_back"
# {"trigger": "go_back", "source": ["show_fsm_pic", "cancel", "value_now", "recommend", "introduction"], "dest": "user"},
# "source" 和 "dest" key 都是來自 list states 中的元素
# "conditions" key 是來自 fsm.py 中的 class TocMachine 定義的函式名稱
# 因此此段代碼要確定 FSM 長甚麼樣子之後，再來修改

# 1202 FSM 以下可能有問題，FSM 是否 deterministic?
# 甚麼條件下，會 go_back
def create_machine():
    machine = TocMachine(
        states=["user", "menu", "introduction", "show_fsm_pic", "search_value_now", "value_now",
                "search_value_full", "value_full", "search_fluctuation", "fluctuation"],
        transitions=[
            {
                "trigger": "advance",
                "source": "user",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "menu",
                "conditions": "is_going_to_menu",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "show_fsm_pic",
                "conditions": "is_going_to_show_fsm_pic",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "introduction",
                "conditions": "is_going_to_introduction",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "search_value_now",
                "conditions": "is_going_to_search_value_now",
            },
            {
                "trigger": "advance",
                "source": "search_value_now",
                "dest": "value_now",
                "conditions": "is_going_to_value_now",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "search_value_full",
                "conditions": "is_going_to_search_value_full",
            },
            {
                "trigger": "advance",
                "source": "search_value_full",
                "dest": "value_full",
                "conditions": "is_going_to_value_full",
            },
            {
                "trigger": "advance",
                "source": "menu",
                "dest": "search_fluctuation",
                "conditions": "is_going_to_search_fluctuation",
            },
            {
                "trigger": "advance",
                "source": "search_fluctuation",
                "dest": "fluctuation",
                "conditions": "is_going_to_fluctuation",
            },
            {
                "trigger": "advance",
                "source": "value_now",
                "dest": "search_value_full",
                "conditions": "is_going_to_search_value_full",
            },
            {"trigger": "go_back", "source": ["introduction", "show_fsm_pic", "value_now", "value_full", "fluctuation"],
             "dest": "menu"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )
    return machine


create_machine().get_graph().draw("fsm.png", prog="dot")
