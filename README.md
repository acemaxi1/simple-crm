# Project Name

Simple-CRM.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)

## Introduction

This is a simple CRM application made for excercise purposes.

## Features

List the key features of the project:

- Filter by Customer
- Table of Products/Orders that you can select
- Orded Summary with total price and quantity

## Installation

Instruction on how to start project:

- Before you start the project make sure you have docker installed and the daemon running.
- After you run the command bellow navigate to your http://localhost:8080/ in any browser.
- There is no need for any database setup since the project uses a sqlite database which is included in the repo with data already prefilled.
- If you lose your data there is sql scripts in the datascripts folder.

```bash
cd root-dir-of-project
docker build -t simple-crm .  
docker run -p 8080:8080 simple-crm
