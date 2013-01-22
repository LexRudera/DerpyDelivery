#include "MenuControls/Button.hpp"
#include "Global.hpp"
#include "Game.hpp"
#include "InputManager.hpp"

namespace me
{
    Button::Button(Menu* parent,
                   const sf::String& text,
                   const sf::Vector2f& size,
                   const sf::Vector2f& pos,
                   float rot) : m_Text(text), m_Btn(size)
    {
        m_Parent = parent;
        // Object properties
        setPosition(pos);
        setRotation(rot);

        // Visual Style
        m_Btn.ApplyStyle(BoxStyle(NULL, sf::Color(128,128,128), sf::Color(85,85,85), 3));

        // Alignment
        m_Text.setPosition(sf::Vector2f(size.x/2-m_Text.getLocalBounds().width/2, size.y/2-m_Text.getCharacterSize()/4*3));//-m_Text.getLocalBounds().height/2));
    }

    Button::~Button()
    {
        //dtor
    }

    void Button::draw(sf::RenderTarget& target, sf::RenderStates states) const
    {
        states.transform *= getTransform();
        target.draw(m_Btn, states);
        target.draw(m_Text, states);
    }

    void Button::tick()
    {
        // Sense the mouse and react accordingly.
        const sf::Vector2i& MPos = Game::Get()->GetInputManager()->GetMousePos();
        if (MPos.x > getPosition().x // Below the x pos
            && MPos.x < getPosition().x + m_Btn.GetSize().x // Above the lower box bounds
            && MPos.y > getPosition().y // Past the y pos
            && MPos.y < getPosition().y + m_Btn.GetSize().y) // Before the right box bounds
        {
            //On Click
            if (Game::Get()->GetInputManager()->IsButtonUp(sf::Mouse::Button::Left))
            {
                // If there is an assigned function or not.
                if (OnClick != 0)
                {
                    (m_Parent->*OnClick)();
                }
            }
            //else
                //Log("Mouse is hovering over '" + m_Text.GetString() + "' - " + to_string(MPos.x) + " - " + to_string(MPos.y));
        }
    }
} // namespace me
