# -*- coding: utf-8 -*-
"""
:author @awhao
cron: 11 6 * * *
new Env('GLaDOS');
"""

import traceback
from typing import Optional

import requests

import utils_data
from notify import send
from utils import get_data

COOKIE_NAMES = ['cookie']

class GLaDOS:
    def __init__(self, check_items: list):
        self.check_items = check_items
        self.original_url = "https://glados.one"
        self.UA = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) "
            "Gecko/20100101 "
            "Firefox/115.0"
        )

    def api_traffic(self, cookies: str):
        traffic_url = f"{self.original_url}/api/user/traffic"
        referer_url = f"{self.original_url}/console"

        with requests.get(
            traffic_url,
            headers={
                "cookie": cookies,
                "referer": referer_url,
                "origin": self.original_url,
                "user-agent": self.UA,
                "content-type": "application/json;charset=UTF-8",
            },
        ) as r:
            return r.json()

    def api_check_in(self, cookies: str) -> dict:
        check_in_url = f"{self.original_url}/api/user/checkin"
        referer_url = f"{self.original_url}/console/checkin"

        payload = {"token": "glados.one"}

        with requests.post(
            check_in_url,
            headers={
                "cookie": cookies,
                "referer": referer_url,
                "origin": self.original_url,
                "user-agent": self.UA,
                "content-type": "application/json;charset=UTF-8",
            },
            json=payload,
        ) as r:
            return r.json()

    def api_status(self, cookies: str) -> dict:
        status_url = f"{self.original_url}/api/user/status"
        referer_url = f"{self.original_url}/console/checkin"

        with requests.get(
            status_url,
            headers={
                "cookie": cookies,
                "referer": referer_url,
                "origin": self.original_url,
                "user-agent": self.UA,
            },
        ) as r:
            return r.json()

    @staticmethod
    def get_budget(vip_level: Optional[int]) -> dict:
        budget_info = utils_data.budget_list
        user_budgets = [
            i
            for i in budget_info
            if (vip_level is not None and i.get("vip") == vip_level)
            or (vip_level is None and "vip" not in i)
        ]
        if user_budgets:
            return user_budgets[0]
        raise OSError(f"Budget info not found for this user! VIP: {vip_level}")

    def checkin(self, cookie):
        try:
            check_in_res = self.api_check_in(cookie)
            check_in_msg = check_in_res["message"]
            if check_in_msg == "\u6ca1\u6709\u6743\u9650":
                msg = (
                    "--------------------\n"
                    "Msg: Your cookies are expired!\n"
                    "--------------------"
                )
                # msg_all += msg
                return msg
            status_res = self.api_status(cookie)
            # print(status_res)
            left_days = int(str(status_res["data"]["leftDays"]).split(".")[0])
            vip_level = status_res["data"]["vip"]
            traffic_res = self.api_traffic(cookie)
            used_gb = traffic_res["data"]["today"] / 1024 / 1024 / 1024
            user_budget = self.get_budget(vip_level)
            total_gb = user_budget["budget"]
            plan = user_budget["level"]
            msg = (
                "--------------------\n"
                f"Msg: {check_in_msg}\n"
                f"Plan: {plan} Plan\n"
                f"Left days: {left_days}\n"
                f"Usage: {used_gb:.3f} GB\n"
                f"Total: {total_gb} GB\n"
                "--------------------"
            )
        except Exception:
            msg = (
                "--------------------\n"
                "Msg: Check in error!\n"
                "Error:\n"
                f"{traceback.format_exc()}\n"
                "--------------------"
            )
        return msg

    def main(self):
        msg_all = ""
        for check_item in self.check_items:
            for cookie_name in COOKIE_NAMES:
                cookie = check_item.get(cookie_name)
                if cookie:
                    msg = self.checkin(cookie)
                else:
                    msg = f"error: cookie {cookie} is not found"
                msg_all += msg + "\n\n"
        return msg_all


if __name__ == "__main__":
    _data = get_data()
    _check_items = _data.get("GLADOS", [])
    result = GLaDOS(check_items=_check_items).main()
    send("GLaDOS", result)