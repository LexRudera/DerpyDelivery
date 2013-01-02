#ifndef DROPDOWNLIST_H
#define DROPDOWNLIST_H

#include <MenuControls\ControlBase.hpp>
#include "MenuControls\Label.hpp"

namespace me
{
    class DropdownList : public ControlBase
    {
        public:
            /** Default constructor */
            DropdownList(unsigned int charSize, const sf::Vector2f& pos = sf::Vector2f(), const sf::Vector2f& size = sf::Vector2f(), float rot = 0);
            /** Default destructor */
            virtual ~DropdownList();

            void tick();
            void draw(sf::RenderTarget& target, sf::RenderStates states) const;

            void Add(const sf::String& text);

            const sf::String& GetSelected() const { return m_Selected.GetString(); }
            void SetSelected(unsigned int i) { m_Selected.SetString(m_Entries[i]); }
        protected:
        private:
            // Private functions
            void OnClick();
            void Open();
            void Close();

            bool m_Down = false;

            // Data
            sf::RectangleShape m_Box;
            std::vector<sf::String> m_Entries;
            Label m_Selected;

            // Temporarily used stuff
            sf::RectangleShape m_SelectionBox;
            std::vector<Label> m_Selections;
    };
} // namespace me

#endif // DROPDOWNLIST_H
