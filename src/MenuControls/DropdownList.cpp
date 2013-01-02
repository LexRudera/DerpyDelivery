#include "MenuControls\DropdownList.hpp"
#include "Game.hpp"
#include "InputManager.hpp"
#include "Global.hpp"

namespace me
{
    DropdownList::DropdownList(unsigned int charSize, const sf::Vector2f& pos, const sf::Vector2f& size, float rot)
    : m_Box(size),
    m_Selected("", charSize, sf::Vector2f(10,size.y/2-charSize/4*3))
    {
        setPosition(pos);

        if (size.x == 0) {
            m_Box.setSize(sf::Vector2f(150,m_Box.getSize().y));
        }
        if (size.y == 0) {
            m_Box.setSize(sf::Vector2f(m_Box.getSize().x, charSize));
            m_Selected.setPosition(sf::Vector2f(10, charSize/2-charSize/4*3));//-m_Text.getLocalBounds().height/2));
        }

        //m_Box.setSize(sf::Vector2f(150, 25));
        m_Box.setFillColor(sf::Color(128,128,128));
        m_Box.setOutlineColor(sf::Color(85,85,85));
        m_Box.setOutlineThickness(2);
        //ctor
    }

    DropdownList::~DropdownList()
    {
        //dtor
    }

    void DropdownList::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Box, states);
        target.draw(m_Selected, states);
        for (unsigned int i = 0; i < m_Selections.size(); i++)
            target.draw(m_Selections[i],states);
    }

    void DropdownList::tick()
    {
        // Sense the mouse and react accordingly.
        const sf::Vector2i& MPos = Game::Get()->GetInputManager()->GetMousePos();
        if (MPos.x > getPosition().x // Below the x pos
            && MPos.x < getPosition().x + m_Box.getSize().x // Above the lower box bounds
            && MPos.y > getPosition().y // Past the y pos
            && MPos.y < getPosition().y + m_Box.getSize().y) // Before the right box bounds
        {
            // On Click
            if (Game::Get()->GetInputManager()->IsButtonUp(sf::Mouse::Button::Left))
            {
                // Shit got clicked!
                OnClick();
            }
            //else
                //Log("Mouse is hovering over '" + m_Text.GetString() + "' - " + to_string(MPos.x) + " - " + to_string(MPos.y));
        }
        else
        {
            if (Game::Get()->GetInputManager()->IsButtonUp(sf::Mouse::Button::Left))
            {
                // There was clicked outside of the control
                Close();
            }
        }
    }

    void DropdownList::OnClick()
    {
        if (m_Down)
        {
        Log("Derp!");
            m_Down = false;
        }
        else
        {
        Log("Herp?");
            m_Down = true;
        }
    }

    void DropdownList::Add(const sf::String& entry)
    {
        m_Entries.push_back(entry);
    }

    void DropdownList::Open()
    {
        unsigned int entries;
    }

    void DropdownList::Close()
    {

    }
} // namespace me
