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
            DropdownList();
            /** Default destructor */
            virtual ~DropdownList();

            void tick();
            void draw(sf::RenderTarget& target, sf::RenderStates states) const;

            void Add(const sf::String& text);

            const sf::String& GetSelected() const { return m_Selected->GetString(); }
        protected:
        private:
            sf::RectangleShape m_Box;

            Label* m_Selected;
            std::vector<Label*> m_Selections;

            bool m_Down;
    };
} // namespace me

#endif // DROPDOWNLIST_H
