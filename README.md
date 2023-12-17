# My Robot CLI for Fast Utilities

<p align="center"><a href="https://ideacat.ro" target="_blank"><img src="https://raw.githubusercontent.com/ideacatlab/my_robot_cli/main/.github/assets/images/robot_cli_logo.svg.svg" width="400" alt="Robot CLI Logo"></a></p>

## About Robot CLI

**Robot CLI** is an interface designed for executing various low-privilege shortcut commands to trigger actions from different utilities. In its current version, it focuses on providing utility commands for MySQL actions.

## Install

Follow these steps to install the script:

1. Clone this repository:

    ```bash
    git clone https://github.com/ideacatlab/my_robot_cli.git
    cd robot
    ```

2. Change the permissions of the install script:

    ```bash
    chmod +x install.sh
    ```

3. Run the install script:

    ```bash
    ./install.sh
    ```

4. Complete the `.env` file with the required environment variables. You can copy the `.env.example` file and fill in the actual values.

## Usage

### Create a Database

To create a MySQL database, use the following command:

```bash
python3 robot.py mysql create <database_name>
```

#### Example:

```bash
python3 robot.py mysql create test_database
```

Expected Output:

```
✅ Database 'test_database' created successfully.
```

### List Databases

To list available MySQL databases, use the following command:

```bash
python3 robot.py mysql list
```

#### Example:

```bash
python3 robot.py mysql list
```

Expected Output:

```
📊 Available databases:

 📀 information_schema
 📀 mysql
 📀 performance_schema
 📀 sys
 📀 test_database
```

## Creating an Alias

You can simplify the usage by creating an alias for Robot CLI. Add the following line to your Zsh configuration file (e.g., `~/.zshrc`):

```bash
alias robot='python3 /path/to/robot.py'
```

Save the file, then restart your Zsh shell or run `source ~/.zshrc` to apply the changes. Now, you can use the `robot` command directly.

#### Example:

```bash
robot mysql create example
```

Expected Output:

```
✅ Database 'example' created successfully.
```

```bash
robot mysql list
```

Expected Output:

```
📊 Available databases:

 📀 example
 📀 information_schema
 📀 mysql
 📀 performance_schema
 📀 sys
 📀 test_database
```

Feel free to replace `/path/to/robot.py` with the actual path to your `robot.py` script. Customize the alias based on your preferences and system setup.

## To do

- [x] mysql create database;
- [x] mysql list databases;
- [] list datatables of certain database;
- [] delete database.

## Security Vulnerabilities

If you discover a security vulnerability within Robot CLI, please send an e-mail to Razvan Gheorghe via [razvan@ideacat.ro](mailto:razvan@ideacat.ro). All security vulnerabilities will be promptly addressed.

## License

Project Robot CLI is covered by MIT License, free of charge.