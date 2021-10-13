#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 15:25:09 2021

@author: hbleie
"""

import streamlit as s
import requests
from operator import itemgetter


s.title("Opensea NFT Galleri")

url = "https://api.opensea.io/api/v1/assets"

sortering = s.selectbox("Sorter etter", ['Navn', 'Token ID', 'Antall salg'])

def writeinfo (assets):
    for asset in assets:
        if asset['name']:
            s.header(asset['name'])
        else:
            s.header(f"{asset['collection']['name']} #{asset['token_id']}")
        s.write(asset['description'])
        s.write("Token ID: " + asset['token_id'])
        s.write("Antall salg: " + str(asset['num_sales']))
        s.write("Pris: " + str(asset['transfer_fee']))
        if asset['image_url'].endswith('mp4') or asset['image_url'].endswith('mov'):
            s.video(asset['image_url'])
        elif asset['image_url'].endswith('svg'):
            s.write('Cannot display SVG-files')
        elif asset['image_url'] == '':
            s.write('No image')
        else:
            s.image(asset['image_url'])
            

if sortering == 'Antall salg':
    respons = requests.get(url)
    r = respons.json()
    assets = sorted(r["assets"], key=itemgetter('num_sales'))
    writeinfo(assets)
  
            
if sortering == 'Token ID':
    respons = requests.get(url)
    r = respons.json()

    assets = sorted(r["assets"], key = itemgetter('token_id'))
    writeinfo(assets)
    
        
if sortering == 'Navn':
    respons = requests.get(url)
    r = respons.json()
    assets = r['assets']
    for asset in assets:
        if not asset['name']:
            asset['name'] = 'unnamed'
    assets = sorted(r["assets"], key=itemgetter('name'))
    writeinfo(assets)
    
            
