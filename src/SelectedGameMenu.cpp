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
        const int height = Game::Get()->GetWindow()->getSize().y-30;
        const int width = height/3*4;
        sf::Vector2f TopLeftPos = sf::Vector2f(Game::Get()->GetWindow()->getSize().x/2-width/2,15);
        Add(m_Box = new StaticBox(sf::Vector2f(width, height),TopLeftPos));
        Add(m_Title = new Label("A Title",30, TopLeftPos + sf::Vector2f(80,20)));
        //Add(m_SubTitle = new Label());
        //Add(m_Author = new Label());
        //Add(m_Email = new Label());
        //Add(m_Website = new Label());
        //Add(m_Description = new Label());
        //Add(m_Saves = new Selector());
        Add(m_Back = new Button(this, "Back"));
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
                /* First one-way iterating way
                if (c == '\n') // Did we hit the end of the line?
                {
                    if (ValidLine)
                    {
                        if (boost::algorithm::to_lower_copy(cat) == "title")
                        {
                            Log(cat);
                            Log(temp);
                            m_Title->SetString(temp.append("\'").insert(0,"\'"));
                        }
                        else if (boost::algorithm::to_lower_copy(cat) == "subtitle")
                        {
                            Log(cat);
                            Log(temp);
                        }
                        else if (boost::algorithm::to_lower_copy(cat) == "description")
                        {
                            Log(cat);
                            Log(temp);
                        }
                        else if (boost::algorithm::to_lower_copy(cat) == "author")
                        {
                            Log(cat);
                            Log(temp);
                        }
                        else if (boost::algorithm::to_lower_copy(cat) == "email")
                        {
                            Log(cat);
                            Log(temp);
                        }
                        else if (boost::algorithm::to_lower_copy(cat) == "website")
                        {
                            Log(cat);
                            Log(temp);
                        }
                        else
                            Log("Undefined Info Category");
                    }
                    cat.clear();
                    temp.clear();
                    ValidLine = false;
                }*/
                if (c == ':')
                {
                    Log("");
                    Log("Hit evaluation point!");
                    std::string ttemp = temp;
                    ttemp.insert(0,"Evaluating:\"").append("\"");
                    Log(ttemp);

                    if (cat.empty()) { // If there is no category on the line
                        /*std::string tcat;

                        // Fill a temporary string to get the category
                        for (std::string::reverse_iterator i = temp.rbegin(); i != temp.rend(); i ++)
                        {
                            if (*i == ' ')
                                break;
                            tcat.push_back(*i);
                        }
                        // Reverse the tcat into the cat
                        for (unsigned int i = 0; i < tcat.size(); i++)
                        {
                            cat.push_back(tcat[tcat.size()-1-i]);
                        }*/

                        cat= temp;
                        // Done. The category is now on the line.
                    }
                    else // We category ready
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
                    temp.clear();
                    /* First one-way iterating way
                    cat = temp;
                    temp.clear();
                    //Log(cat);
                    ValidLine = true;*/
                    Log("");
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
        if (boost::algorithm::to_lower_copy(category) == "title")
        {
            Log(category);
            Log(data);
            m_Title->SetString(data.append("\'").insert(0,"\'"));
        }
        else if (boost::algorithm::to_lower_copy(category) == "subtitle")
        {
            Log(category);
            Log(data);
        }
        else if (boost::algorithm::to_lower_copy(category) == "description")
        {
            Log(category);
            Log(data);
        }
        else if (boost::algorithm::to_lower_copy(category) == "author")
        {
            Log(category);
            Log(data);
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
