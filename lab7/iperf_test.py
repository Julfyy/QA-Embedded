#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 23:38:35 2022

@author: bohdan
"""
import parser


class TestSuite():
    def test_iperf3(self, client):
        stdout, error, err_serv = client
        # print('Received from fixture client is:\n{}'.format(stdout.decode("UTF-8")))
        assert error != 0, "Error connect"
        assert err_serv != 0, "Error start server"
        assert 0 == 0, "Error"

        dict = parser.parser(stdout)
        for i in range(len(dict)):
            assert float(dict[i][1]) > 200 and float(dict[i][2]) > 1

        return
