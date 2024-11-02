{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWjntpr+rjPf333xS+OUa3",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sanarazaaa/Allergy_detector/blob/main/Allergy_Detector.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 26,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "F_CyW6kDmtkT",
        "outputId": "99a4dbca-0c2e-493b-bc0e-1860e45bd3e1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-11-02 09:51:22.644 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.738 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2024-11-02 09:51:22.741 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.744 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.746 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.752 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.753 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.755 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.756 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.757 Session state does not function when running a script without `streamlit run`\n",
            "2024-11-02 09:51:22.761 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.763 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.765 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.767 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.769 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.771 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.773 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.774 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.776 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.778 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.779 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.781 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.782 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.784 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.786 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.788 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.789 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.791 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.792 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.794 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.796 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.798 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.799 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.800 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.802 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.803 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.804 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.806 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.812 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.816 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-02 09:51:22.819 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "class AllergyChecker:\n",
        "    def __init__(self):\n",
        "        self.allergen_mapping = {\n",
        "            'peanut butter': ['peanuts'],\n",
        "            'milk': ['dairy'],\n",
        "            'shrimp': ['shellfish'],\n",
        "            'bread': ['gluten'],\n",
        "            'cheese': ['dairy'],\n",
        "            'soy sauce': ['soy'],\n",
        "            'egg salad': ['eggs'],\n",
        "            'almond milk': ['almonds'],\n",
        "            'soy milk': ['soy'],\n",
        "            'wheat bread': ['gluten'],\n",
        "            'yogurt': ['dairy'],\n",
        "            'salmon': ['fish'],\n",
        "            'chocolate': ['dairy', 'nuts'],\n",
        "            'hummus': ['chickpeas'],\n",
        "            'coconut milk': ['coconut'],\n",
        "            'tofu': ['soy'],\n",
        "            'salsa': ['tomato', 'onion'],\n",
        "            'butter': []\n",
        "        }\n",
        "        self.user_profile = {}\n",
        "\n",
        "    def set_allergies(self, username, allergies):\n",
        "        self.user_profile[username] = [allergy.strip().lower() for allergy in allergies.split(',')]\n",
        "        return f\"Allergy profile updated for {username}.\"\n",
        "\n",
        "    def predict_ingredients(self):\n",
        "        return list(self.allergen_mapping.keys())\n",
        "\n",
        "    def check_allergy(self, username):\n",
        "        detected_ingredients = self.predict_ingredients()\n",
        "        user_allergies = self.user_profile.get(username, [])\n",
        "\n",
        "        matched_allergens = []\n",
        "        for ingredient in detected_ingredients:\n",
        "            if ingredient in self.allergen_mapping:\n",
        "                allergens = self.allergen_mapping[ingredient]\n",
        "                if any(allergen in user_allergies for allergen in allergens):\n",
        "                    matched_allergens.append(ingredient)\n",
        "\n",
        "        if matched_allergens:\n",
        "            ingredients_list = \"<br>\".join(['🚫 ' + ingredient for ingredient in matched_allergens])\n",
        "            result_text = (f\"<strong style='color: red;'>This food is dangerous!</strong><br><br>\"\n",
        "                           f\"Oh, honey, put that fork down!<br><br>\"\n",
        "                           f\"You don’t want to play with fire, do you?<br><br>\"\n",
        "                           f\"That could make you <strong>seriously ill</strong>! 😱<br><br>\"\n",
        "                           f\"Let’s spill the tea on what’s in that dish:<br>{ingredients_list}<br><br>\"\n",
        "                           f\"And listen up! You absolutely *have* to steer clear of these party crashers! 🥳\")\n",
        "            sound_file = \"alert_sound.mp3\"  # Path to the alert sound file\n",
        "        else:\n",
        "            ingredients_list = \"<br>\".join([f\"✓ {ingredient}\" for ingredient in detected_ingredients])\n",
        "            result_text = (f\"<strong>🟢 Safe to Eat!</strong><br><br>\"\n",
        "                           f\"<strong>Detected Ingredients:</strong><br>{ingredients_list}<br><br>\"\n",
        "                           f\"This food is good for you! 😊<br><br>\"\n",
        "                           f\"Now go ahead and feast, darling! ✨\")\n",
        "            sound_file = \"safe_sound.mp3\"  # Path to the safe sound file\n",
        "\n",
        "        return result_text, sound_file\n",
        "\n",
        "# Instantiate the AllergyChecker\n",
        "allergy_checker = AllergyChecker()\n",
        "\n",
        "# Streamlit Application\n",
        "st.title(\"User Allergy Profile Setup and Allergy Checker with Sound Alerts\")\n",
        "\n",
        "# Setup Profile Tab\n",
        "st.header(\"Setup Profile\")\n",
        "username_input = st.text_input(\"Enter Username\")\n",
        "allergies_input = st.text_input(\"Enter Allergies (comma-separated)\", placeholder=\"e.g., peanuts, dairy\")\n",
        "if st.button(\"Set/Update Allergy Profile\"):\n",
        "    profile_update_status = allergy_checker.set_allergies(username_input, allergies_input)\n",
        "    st.success(profile_update_status)\n",
        "\n",
        "# Check Food Allergies Tab\n",
        "st.header(\"Check Food Allergies\")\n",
        "username_input_check = st.text_input(\"Enter Username for Allergy Check\")\n",
        "food_image = st.file_uploader(\"Upload an image of the food\", type=['jpg', 'jpeg', 'png'])\n",
        "if st.button(\"Check Allergy\"):\n",
        "    if food_image is not None:\n",
        "        text, sound_file = allergy_checker.check_allergy(username_input_check)\n",
        "        st.markdown(text, unsafe_allow_html=True)\n",
        "        st.audio(sound_file)  # Play the appropriate sound file\n",
        "    else:\n",
        "        st.warning(\"Please upload an image of the food.\")\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E9gbLGPTSI-1",
        "outputId": "02fa1291-1fd0-4e7a-d6ef-9ee818d00398"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.39.0-py2.py3-none-any.whl.metadata (8.5 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/lib/python3/dist-packages (from streamlit) (1.4)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.1)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<11,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (10.4.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.9.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Collecting watchdog<6,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-5.0.3-py3-none-manylinux2014_x86_64.whl.metadata (41 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m41.9/41.9 kB\u001b[0m \u001b[31m2.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.20.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.39.0-py2.py3-none-any.whl (8.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.7/8.7 MB\u001b[0m \u001b[31m48.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m69.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-5.0.3-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.3/79.3 kB\u001b[0m \u001b[31m6.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.39.0 watchdog-5.0.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import gradio as gr"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 314
        },
        "id": "lKJbl4F2ng1p",
        "outputId": "280c7964-3a33-4a16-b869-df90d24b00e4"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ModuleNotFoundError",
          "evalue": "No module named 'gradio'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-43eca54f7d45>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mimport\u001b[0m \u001b[0mgradio\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mgr\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'gradio'",
            "",
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0;32m\nNOTE: If your import is failing due to a missing package, you can\nmanually install dependencies using either !pip or !apt.\n\nTo view examples of installing some common dependencies, click the\n\"Open Examples\" button below.\n\u001b[0;31m---------------------------------------------------------------------------\u001b[0m\n"
          ],
          "errorDetails": {
            "actions": [
              {
                "action": "open_url",
                "actionText": "Open Examples",
                "url": "/notebooks/snippets/importing_libraries.ipynb"
              }
            ]
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install gradio\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xe2P_fHgntwD",
        "outputId": "843c1f92-76a6-46ba-dcde-fddbf90f66a0"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting gradio\n",
            "  Downloading gradio-5.4.0-py3-none-any.whl.metadata (16 kB)\n",
            "Collecting aiofiles<24.0,>=22.0 (from gradio)\n",
            "  Downloading aiofiles-23.2.1-py3-none-any.whl.metadata (9.7 kB)\n",
            "Requirement already satisfied: anyio<5.0,>=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.7.1)\n",
            "Collecting fastapi<1.0,>=0.115.2 (from gradio)\n",
            "  Downloading fastapi-0.115.4-py3-none-any.whl.metadata (27 kB)\n",
            "Collecting ffmpy (from gradio)\n",
            "  Downloading ffmpy-0.4.0-py3-none-any.whl.metadata (2.9 kB)\n",
            "Collecting gradio-client==1.4.2 (from gradio)\n",
            "  Downloading gradio_client-1.4.2-py3-none-any.whl.metadata (7.1 kB)\n",
            "Requirement already satisfied: httpx>=0.24.1 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.27.2)\n",
            "Collecting huggingface-hub>=0.25.1 (from gradio)\n",
            "  Downloading huggingface_hub-0.26.2-py3-none-any.whl.metadata (13 kB)\n",
            "Requirement already satisfied: jinja2<4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.1.4)\n",
            "Collecting markupsafe~=2.0 (from gradio)\n",
            "  Downloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.0 kB)\n",
            "Requirement already satisfied: numpy<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (1.26.4)\n",
            "Requirement already satisfied: orjson~=3.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (3.10.10)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.10/dist-packages (from gradio) (24.1)\n",
            "Requirement already satisfied: pandas<3.0,>=1.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.2.2)\n",
            "Requirement already satisfied: pillow<12.0,>=8.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (10.4.0)\n",
            "Requirement already satisfied: pydantic>=2.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (2.9.2)\n",
            "Collecting pydub (from gradio)\n",
            "  Downloading pydub-0.25.1-py2.py3-none-any.whl.metadata (1.4 kB)\n",
            "Collecting python-multipart==0.0.12 (from gradio)\n",
            "  Downloading python_multipart-0.0.12-py3-none-any.whl.metadata (1.9 kB)\n",
            "Requirement already satisfied: pyyaml<7.0,>=5.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (6.0.2)\n",
            "Collecting ruff>=0.2.2 (from gradio)\n",
            "  Downloading ruff-0.7.2-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (25 kB)\n",
            "Collecting safehttpx<1.0,>=0.1.1 (from gradio)\n",
            "  Downloading safehttpx-0.1.1-py3-none-any.whl.metadata (4.1 kB)\n",
            "Collecting semantic-version~=2.0 (from gradio)\n",
            "  Downloading semantic_version-2.10.0-py2.py3-none-any.whl.metadata (9.7 kB)\n",
            "Collecting starlette<1.0,>=0.40.0 (from gradio)\n",
            "  Downloading starlette-0.41.2-py3-none-any.whl.metadata (6.0 kB)\n",
            "Collecting tomlkit==0.12.0 (from gradio)\n",
            "  Downloading tomlkit-0.12.0-py3-none-any.whl.metadata (2.7 kB)\n",
            "Requirement already satisfied: typer<1.0,>=0.12 in /usr/local/lib/python3.10/dist-packages (from gradio) (0.12.5)\n",
            "Requirement already satisfied: typing-extensions~=4.0 in /usr/local/lib/python3.10/dist-packages (from gradio) (4.12.2)\n",
            "Collecting uvicorn>=0.14.0 (from gradio)\n",
            "  Downloading uvicorn-0.32.0-py3-none-any.whl.metadata (6.6 kB)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.10/dist-packages (from gradio-client==1.4.2->gradio) (2024.10.0)\n",
            "Collecting websockets<13.0,>=10.0 (from gradio-client==1.4.2->gradio)\n",
            "  Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.6 kB)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (1.3.1)\n",
            "Requirement already satisfied: exceptiongroup in /usr/local/lib/python3.10/dist-packages (from anyio<5.0,>=3.0->gradio) (1.2.2)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (2024.8.30)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.10/dist-packages (from httpx>=0.24.1->gradio) (1.0.6)\n",
            "Requirement already satisfied: h11<0.15,>=0.13 in /usr/local/lib/python3.10/dist-packages (from httpcore==1.*->httpx>=0.24.1->gradio) (0.14.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.25.1->gradio) (3.16.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.25.1->gradio) (2.32.3)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.10/dist-packages (from huggingface-hub>=0.25.1->gradio) (4.66.6)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3.0,>=1.0->gradio) (2024.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.23.4 in /usr/local/lib/python3.10/dist-packages (from pydantic>=2.0->gradio) (2.23.4)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (8.1.7)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from typer<1.0,>=0.12->gradio) (13.9.3)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3.0,>=1.0->gradio) (1.16.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (2.18.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.25.1->gradio) (3.4.0)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->huggingface-hub>=0.25.1->gradio) (2.2.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio) (0.1.2)\n",
            "Downloading gradio-5.4.0-py3-none-any.whl (56.7 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m56.7/56.7 MB\u001b[0m \u001b[31m19.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading gradio_client-1.4.2-py3-none-any.whl (319 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m319.8/319.8 kB\u001b[0m \u001b[31m23.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading python_multipart-0.0.12-py3-none-any.whl (23 kB)\n",
            "Downloading tomlkit-0.12.0-py3-none-any.whl (37 kB)\n",
            "Downloading aiofiles-23.2.1-py3-none-any.whl (15 kB)\n",
            "Downloading fastapi-0.115.4-py3-none-any.whl (94 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m94.7/94.7 kB\u001b[0m \u001b[31m7.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading huggingface_hub-0.26.2-py3-none-any.whl (447 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m447.5/447.5 kB\u001b[0m \u001b[31m31.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading MarkupSafe-2.1.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (25 kB)\n",
            "Downloading ruff-0.7.2-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.0/11.0 MB\u001b[0m \u001b[31m98.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading safehttpx-0.1.1-py3-none-any.whl (8.4 kB)\n",
            "Downloading semantic_version-2.10.0-py2.py3-none-any.whl (15 kB)\n",
            "Downloading starlette-0.41.2-py3-none-any.whl (73 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m73.3/73.3 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading uvicorn-0.32.0-py3-none-any.whl (63 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m63.7/63.7 kB\u001b[0m \u001b[31m4.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading ffmpy-0.4.0-py3-none-any.whl (5.8 kB)\n",
            "Downloading pydub-0.25.1-py2.py3-none-any.whl (32 kB)\n",
            "Downloading websockets-12.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (130 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m130.2/130.2 kB\u001b[0m \u001b[31m9.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pydub, websockets, uvicorn, tomlkit, semantic-version, ruff, python-multipart, markupsafe, ffmpy, aiofiles, starlette, huggingface-hub, safehttpx, gradio-client, fastapi, gradio\n",
            "  Attempting uninstall: markupsafe\n",
            "    Found existing installation: MarkupSafe 3.0.2\n",
            "    Uninstalling MarkupSafe-3.0.2:\n",
            "      Successfully uninstalled MarkupSafe-3.0.2\n",
            "  Attempting uninstall: huggingface-hub\n",
            "    Found existing installation: huggingface-hub 0.24.7\n",
            "    Uninstalling huggingface-hub-0.24.7:\n",
            "      Successfully uninstalled huggingface-hub-0.24.7\n",
            "Successfully installed aiofiles-23.2.1 fastapi-0.115.4 ffmpy-0.4.0 gradio-5.4.0 gradio-client-1.4.2 huggingface-hub-0.26.2 markupsafe-2.1.5 pydub-0.25.1 python-multipart-0.0.12 ruff-0.7.2 safehttpx-0.1.1 semantic-version-2.10.0 starlette-0.41.2 tomlkit-0.12.0 uvicorn-0.32.0 websockets-12.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import gradio as gr\n"
      ],
      "metadata": {
        "id": "uQOXr7wQn0Us"
      },
      "execution_count": 4,
      "outputs": []
    }
  ]
}
