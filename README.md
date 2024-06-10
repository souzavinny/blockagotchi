# Blockagotchi

Blockagotchi is a blockchain-based game that brings the nostalgia of Tamagotchi to the Web3 era. Users can create, care for, and evolve their virtual pets called Blockagotchi. This application uses Cartesi Rollups for its backend, making it a scalable and secure DApp.

## Table of Contents

-   [Features](#features)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Project Structure](#project-structure)
-   [Contributing](#contributing)
-   [License](#license)

## Features

-   **Creation (Birth):** Users can create a Blockagotchi by purchasing an egg with tokens.
-   **Feeding:** Blockagotchis can eat four types of food - Fish, Meat, Vegetables, and Fruit, which affect their evolution and health.
-   **Day Care:** Users can bathe their Blockagotchis and take them for walks to increase happiness and health.
-   **Evolution:** Blockagotchis evolve through stages: Blob, Child, Teen, Adult, and Old.
-   **Ranking:** Users can rank their Blockagotchis based on their overall score, which is a sum of their age and happiness.
-   **Shopping:** Users can purchase items to enhance their Blockagotchis.

## Installation

### Prerequisites
- Cartesi CLI
-   Python 3.8+
-   Pip

### Clone the Repository

```bash
git clone https://github.com/souzavinny/blockagotchi.git
cd blockagotchi` 
```

### Set Up the Environment
With Cartesi CLI installed, just run in the root folder:
```bash
cartesi build
```
### Environment Variables

Create a `.env` file in the root directory and add the following environment variables:

```bash
`ROLLUP_HTTP_SERVER_URL=http://localhost:8080/rollup` 
```
## Usage

### Running the Application

Start the Cartesi Rollups server (ensure it's running locally):

```bash
cartesi run
```

### Advance states jsons (To be converted by the frontend)

#### Testar criação de BlockaGotchi (Usuario precisa ter ether depositado)
{
    "action": "create_blockagotchi",
    "name": "Gottito"
}
#### Testar alimentação de Blockagotchi
{
    "action": "feed_blockagotchi",
    "food_type": "Peixe"
}
#### Testar caminhada
{
    "action": "walk_blockagotchi",
    "walk_type": "corrida"
}
#### Testar banho
{
    "action": "bathe_cartgotchi",
    "bath_type": "normal",
    "is_paid": "False"
}
#### Shopping
##### Comprar
{
    "action": "buy_item",
    "item_id": 1
}
##### Aplicar
{
    "action": "apply_item",
    "item_id": 1
}

### Inspecting the State endpoints

#### To get the balance:
localhost:8080/inspect/balance/ether/:address
#### To get user blockagotchi info:
localhost:8080/inspect/user_blockagotchi/:address
#### To get all blockagotchi info:
localhost:8080/inspect/all_blockagotchis
#### To get blockagotchi info by id:
localhost:8080/inspect/blockagotchi
#### To get all shop items list
localhost:8080/inspect/shop_items
#### To get all blockagotchis ranked by score
localhost:8080/inspect/ranking


## Project Structure

```bash

`blockagotchi/
│
├──handlers
		└── advance/
		│   	└── advance_handler.py
		└──inspect/
│   	 		└── inspect_handler.py
├── blockagotchi.py
├── user.py
├── shop.py
├── dapp.py
├── requirements.txt
├── README.md
└── .env` 
```

## Contributing

We welcome contributions! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch.
3.  Make your changes.
4.  Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
