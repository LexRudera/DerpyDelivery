#include "MenuControls\DropdownList.hpp"

namespace me
{
    DropdownList::DropdownList()
    {
        //ctor
    }

    DropdownList::~DropdownList()
    {
        //dtor
    }

    void DropdownList::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Btn, states);
        target.draw(m_Text, states);
        for (unsigned int i = 0; i < m_Selections.size(); i++)
            target.draw(*m_Selections[i],states);
    }

    void DropdownList::tick()
    {
        // Sense the mouse and react accordingly.
        sf::Vector2i MPos = Game::Get()->GetInputManager()->GetMousePos();
        if (MPos.x > getPosition().x // Below the x pos
            && MPos.x < getPosition().x + m_Btn.getSize().x // Above the lower box bounds
            && MPos.y > getPosition().y // Past the y pos
            && MPos.y < getPosition().y + m_Btn.getSize().y) // Before the right box bounds
        {
            //On Click
            if (Game::Get()->GetInputManager()->IsButtonUp(sf::Mouse::Button::Left))
            {
                //Shit got clicked!
            }
            //else
                //Log("Mouse is hovering over '" + m_Text.GetString() + "' - " + to_string(MPos.x) + " - " + to_string(MPos.y));
        }
    }
} // namespace me
