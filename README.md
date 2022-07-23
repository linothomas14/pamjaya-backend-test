# Backend Pamjaya API

This API is intended for the purposes of our BotChat Keluhan project at Pamjaya Hackathon 2022

## Table of Contents

- [Setup](#setup)
- [Routes](#routes)
- [API Documentation](#api-documentation)
- [Contributor](#contributor)

## Setup

To run this project, follow these steps:

- run `pip install -r requirements.txt` to install dependencies
- run `cp .env-example .env`
- setup .env to handle connection with database
- run `flask db init`
- run `flask db migrate`
- run `flask db upgrade`
- run `flask run`

## Routes

| HTTP METHOD                        |             POST             |                GET                 |      PUT       |     DELETE     |
| ---------------------------------- | :--------------------------: | :--------------------------------: | :------------: | :------------: |
| /pelanggans                        |              -               |         List of Pelanggan          |       -        |       -        |
| /pelanggans/`<string:id>`          |              -               |        Detail of Pelanggan         |       -        |       -        |
| /keluhans                          |         Add keluhan          |          List of keluhans          |       -        |       -        |
| /keluhans/`<string:id>`            |              -               |           Detail keluhan           | Update keluhan | Delete keluhan |
| /keluhans?page=`<string>`          |              -               |      List of keluhan per Page      |       -        |       -        |
| /keluhans?jenis_keluhan=`<string>` |              -               | List of Keluhans per jenis_keluhan |       -        |       -        |
| /sendOTP                           | send OTP to pelanggan number |                 -                  |       -        |       -        |
| /login                             |       pelanggan login        |                 -                  |       -        |       -        |
| /register                          |      pelanggan register      |                 -                  |       -        |       -        |

## API Documentation

### List of Endpoints

- [Auth](#auth)
  - [sendOTP](#sendOTP)
  - [register](#register)
  - [login](#login)
- [Pelanggan](#pelanggan)
  - [Get All Pelanggans](#get-all-pelanggans)
  - [Get Pelanggan by Id](#get-pelanggan-by-id)
- [Keluhan](#keluhan)
  - [Get All Keluhans or By Page](#get-all-keluhans-or-by-page)
  - [Get Keluhans By Category](#get-keluhans-by-jenis_keluhan)
  - [Get Keluhan By Id](#get-keluhan-by-id)
  - [Add Keluhan](#add-keluhan)
  - [Update Keluhan](#update-keluhan)
  - [Delete Keluhan](#delete-keluhan)

## Auth

### sendOTP

- Method : POST
- URL : `/sendOTP`
- Request body :

```json
{
  "id_pelanggan": "100001"
}
```

- Response body :

```json
{
  "message": "OTP dikirim ke nomor +6283872750005",
  "values": []
}
```

### Register

- Method : POST
- URL : `/register`
- Request body :

```json
{
  "id_pelanggan": "100001",
  "password": "admin123",
  "otp_code": "953863"
}
```

- Response body :

````json
{
  "message": "register success",
  "values": []
}


### Login

- Method : POST
- URL : `/login`
- Request body :

```json
{
  "id_pelanggan": "1",
  "password": "admin123"
}
````

- Response body :

```json
{
  "message": "Berhasil login",
  "values": {
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY1ODQyODI5MiwianRpIjoiMjliMWIzZmUtNTBjMC00ODdkLWFlMDYtOThkODk4NzYzMGZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJpZCI6IjEifSwibmJmIjoxNjU4NDI4MjkyLCJleHAiOjE2NTg0MjkxOTJ9.7fcq2sGZtHURmN2EEZLWI7XX4fmJbsR6XFdIar9l7z4"
  }
}
```

## Pelanggan

### Get All Pelanggans

- Method : GET
- URL : `/pelanggans`
- Response body :

```json
{
  "message": "",
  "values": [
    {
      "alamat": "PERUM BUKIT GOLF HIJAU",
      "id_pelanggan": "101",
      "kecamatan": "BABAKAN MADANG",
      "kelurahan": "CIJAYANTI",
      "kode_pos": "16810",
      "kota_madya": "KAB BOGOR",
      "nama": "YULYANO THOMAS DJAYA",
      "no_hp": "83872750005"
    }
  ]
}
```

## Keluhan

### Get All Keluhans or By Page

- Method : GET
- URL : `/keluhans` or `/keluhans?page=<int>`
- Response body :

```json
{
  "message": "",
  "values": [
    {
      "created_at": "Fri, 22 Jul 2022 00:57:40 GMT",
      "id": "111fd5fb-24e6-48cd-a3cc-f91194f73322",
      "id_pelanggan": "1",
      "jenis_keluhan": "AIR MATI",
      "kecamatan": "BABAKAN MADANG",
      "keluhan": "Pak tolong air di daerah sentul mati",
      "kelurahan": "CIJAYANTI",
      "kode_pos": "16810",
      "kota_madya": "KAB BOGOR",
      "updated_at": "Fri, 22 Jul 2022 00:57:40 GMT"
    }
  ]
}
```

### Get Keluhans By Jenis Keluhan

- Method : GET
- URL : `/keluhans?jenis_keluhan=<string>`
- Response body :

```json
{
  "message": "",
  "values": [
    {
      "created_at": "Fri, 22 Jul 2022 00:57:40 GMT",
      "id": "111fd5fb-24e6-48cd-a3cc-f91194f73322",
      "id_pelanggan": "1",
      "jenis_keluhan": "AIR MATI",
      "kecamatan": "BABAKAN MADANG",
      "keluhan": "Pak tolong air di daerah sentul mati",
      "kelurahan": "CIJAYANTI",
      "kode_pos": "16810",
      "kota_madya": "KAB BOGOR",
      "updated_at": "Fri, 22 Jul 2022 00:57:40 GMT"
    }
  ]
}
```

### Get Keluhan By Id

- Method : GET
- URL : `/keluhans/<string:id>`
- Response body :

```json
{
  "message": "",
  "values": [
    {
      "created_at": "Fri, 22 Jul 2022 00:57:40 GMT",
      "id": "111fd5fb-24e6-48cd-a3cc-f91194f73322",
      "id_pelanggan": "1",
      "jenis_keluhan": "AIR MATI",
      "kecamatan": "BABAKAN MADANG",
      "keluhan": "Pak tolong air di daerah sentul mati",
      "kelurahan": "CIJAYANTI",
      "kode_pos": "16810",
      "kota_madya": "KAB BOGOR",
      "updated_at": "Fri, 22 Jul 2022 00:57:40 GMT"
    }
  ]
}
```

### Add Keluhan

- Method : POST
- URL : `/keluhans`
- Request body :

```json
{
  "jenis_keluhan": "AIR MATI",
  "keluhan": "PAK AIR DI RUMAH SAYA MATI NIH",
  "kelurahan": "CIJAYANTI",
  "kecamatan": "BABAKAN MADANG",
  "kota_madya": "KAB BOGOR",
  "kode_pos": "16810"
}
```

- Response body:

```json
{
  "message": "Keluhan added",
  "values": ""
}
```

### Update Keluhan

- Method : PUT
- URL : `/keluhans/<string:id>`

- Response body:
  `status code 201`

```json
{
  "message": "successfully updated",
  "values": ""
}
```

### Delete Keluhan

- Method : DELETE
- URL : `/keluhans/<string:id>`
- Response body :

```json
{
  "message": "keluhan deleted",
  "values": ""
}
```

## Status Code

returns the following status codes in its API:

| Status Code | Description   |
| :---------- | :------------ |
| 200         | `OK`          |
| 201         | `CREATED`     |
| 400         | `BAD REQUEST` |
| 404         | `NOT FOUND`   |

## Contributor

1. Yulyano Thomas Djaya (C20090F998)
