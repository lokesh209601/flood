# [CDAC Flood Prediction](https://github.com/akashlende/cdac-frontend)

The project is divided into two parts:

1. [React frontend](https://github.com/akashlende/cdac-frontend)
2. [Flask server](https://github.com/akashlende/cdac-backend)

## React frontend

A fast and easy to use frontend build using ReactJS.

### How to install?

1. Prerequisites

-   [Node JS](https://nodejs.org/en/download/) 12 and above
-   [yarn](https://classic.yarnpkg.com/en/docs/install/#windows-stable) package manager (optional)

2. Clone the frontend repository

```
git clone https://github.com/akashlende/cdac-frontend.git
cd cdac-frontend`
```

3.  Install the dependencies

```
npm install
```

or

```
yarn
```

4. Configure the backend
   Edit `src/config.js` for pointing to the flask server. If the frontend and backend are on the same machine leave this field to `http://localhost:5000`, else, change it to domain where server is hosted on.

5. Once the dependencies are installed, run the code.

```
npm start
```

or

```
yarn start
```

### How to build?

1. Edit `package.json`. Set the value of `homepage` to address where you want to deploy the frontend. For example,

```
{
    "name": "cdac-flood-prediction",
    "version": "1.2.0",
    "homepage": "https://sample.com/flood-predict/",
    ...
    ...
```

2. Create a production build

```
npm run-script build
```

or

```
yarn build
```

Voila! The production build is ready to be deployed. Production build is in `build` directory.

## Flask Server

Multi-threaded flask server which features FBProphet and LDA at it's kernel to predict floods.

### How to install?

1. Prerequisites

-   [Anaconda](https://www.anaconda.com/products/individual#Downloads)

2. Clone the backend repository

```
git clone https://github.com/akashlende/cdac-backend.git
cd cdac-backend`
```

3. Install dependencies

```
conda create --name <env_name> --file requirements.txt
```

4. Activate the conda environment

```
conda activate <env_name>
```

5. Run flask server
   Specify the port for the flask server to run on in file `main.py`. And then run the server.

```
python main.py
```

## Teammates
[Parag Ghorpade](https://github.com/Parag0506) 
[Akash Lende](https://github.com/akashlende)
[Aditya Gadge](https://github.com/Aditya25000)
[Hitesh Chordiya](https://github.com/Hitesh-Chordiya) 
