# Project Name

Simple-CRM.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)

## Introduction

This is a simple CRM application made for exercise purposes.

## Features

List of key features of the project:

- Filter by Customer
- Table of Products/Orders that you can select
- Order Summary with total price and quantity

## Installation

Instructions on how to start the project:

- Before you start the project, make sure you have Docker installed and the daemon running.
- After you run the command below, navigate to http://localhost:8080/ in any browser.
- There is no need for any database setup since the project uses an SQLite database, which is included in the repo with data already prefilled.
- If you lose your data, there are SQL scripts in the `datascripts` folder.

```bash
cd root-dir-of-project
docker build -t simple-crm .  
docker run -p 8080:8080 simple-crm
