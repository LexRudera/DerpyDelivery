#include "SelectedGameMenu.hpp"
#include "Game.hpp"
#include "GameMenu.hpp"
#include "Global.hpp"
#include <fstream>
#include <regex>
#include <boost/algorithm/string/case_conv.hpp>

namespace me
{
    SelectedGameMenu::SelectedGameMenu(const boost::filesystem::path& path)
    {
        m_Path = path;
    }

    SelectedGameMenu::~SelectedGameMenu()
    {

    }

    void SelectedGameMenu::Load()
    {
        // Element creation
        sf::Vector2f Size = sf::Vector2f((Game::Get()->GetWindow()->getSize().y-30)/3*4, (Game::Get()->GetWindow()->getSize().y-30));
        sf::Vector2f TopLeftPos = sf::Vector2f(Game::Get()->GetWindow()->getSize().x/2-Size.x/2,15);
        Add(m_Box = new StaticBox(Size, TopLeftPos));
        Add(m_Title = new Label("Title", 50, TopLeftPos + sf::Vector2f(80,30)));
        Add(m_SubTitle = new Label("Subtitle", 25, TopLeftPos + sf::Vector2f(90,80)));
        Add(m_Author = new Label("Author", 20, TopLeftPos + sf::Vector2f(70,20)));
        //Add(m_Email = new Label());
        //Add(m_Website = new Label());
        Add(m_Description = new Label("Description", 20, TopLeftPos + sf::Vector2f(50,120)));
        //Add(m_Saves = new Selector());
        Add(m_Back = new Button(this, "Back", sf::Vector2f(150,50), TopLeftPos + Size - sf::Vector2f(200,100)));
        //Add(m_Load = new Button(this, "Load Save"));
        //Add(m_Delete = new Button(this, "Delete Save"));
        //Add(m_Play = new Button(this, "Play"));

        // Event Functions
        m_Back->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Back_OnClick));
        /*m_Load->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Load_OnClick));
        m_Delete->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Delete_OnClick));
        m_Play->SetOnClickFunction(static_cast<MenuEvent>(&SelectedGameMenu::m_Play_OnClick));*/

        // Update with game info
        ReadGameinfo();
    }

    void SelectedGameMenu::ReadGameinfo()
    {
        Log("-READING GAME INFO-");
        // Open a Filestream
        std::ifstream file(m_Path.string() + "\\gameinfo.txt");
        char c;
        std::string temp, cat;
        bool ValidLine = false;
        // Let's iterate through the file!
        while (file.good())
        {
            file.get(c); // Get the next characters
            if (file.good()) // Are we good?
            {
                if (c == ':')
                {
                    if (cat.empty()) { // If there is no category on the line
                        // Assign the buffer into the catagory.
                        cat = temp;
                    }
                    else // We have a category ready
                    {
                        // Find split point between the future category and data
                        int SplitPoint = temp.find_last_of('\n');
                        // Extract the new category
                        std::string tcat = temp.substr(SplitPoint+1);
                        // Extract the data for the current category
                        temp = temp.substr(0,SplitPoint);

                        // Apply the extracted data into the stored category
                        ApplyData(cat, temp);

                        // Set the new category
                        cat = tcat;
                        Log(to_string(cat.size()));
                    }
                    // Clear the buffer
                    temp.clear();
                }
                else
                    if (temp.empty() && c == ' '){}
                    else
                    temp.push_back(c);

            }
            else // End of file or weirdass error
            {
                // Apply the extracted data into the stored category
                ApplyData(cat, temp);
            }
        }
        Log("-END-");
    }

    void SelectedGameMenu::ApplyData(const std::string& category, std::string data)
    {
        Log("Setting data on a category");
        Log(category);
        //data.append("\'").insert(0,"\'");
        if (boost::algorithm::to_lower_copy(category) == "title")
        {
            Log(category);
            Log(data);
            m_Title->SetString(data);
        }
        else if (boost::algorithm::to_lower_copy(category) == "subtitle")
        {
            Log(category);
            Log(data);
            m_SubTitle->SetString(data);
        }
        else if (boost::algorithm::to_lower_copy(category) == "description")
        {
            Log(category);
            Log(data);
            m_Description->SetString(data);
        }
        else if (boost::algorithm::to_lower_copy(category) == "author")
        {
            Log(category);
            Log(data);
            m_Author->SetString(data.append("\'s"));
        }
        else if (boost::algorithm::to_lower_copy(category) == "email")
        {
            Log(category);
            Log(data);
        }
        else if (boost::algorithm::to_lower_copy(category) == "website")
        {
            Log(category);
            Log(data);
        }
        else
            Log("Undefined Info Category");
    }

    void SelectedGameMenu::m_Back_OnClick()
    {
        Game::Get()->ChangeScene(new GameMenu());
    }

    void SelectedGameMenu::m_Load_OnClick()
    {

    }

    void SelectedGameMenu::m_Delete_OnClick()
    {

    }

    void SelectedGameMenu::m_Play_OnClick()
    {

    }
}
