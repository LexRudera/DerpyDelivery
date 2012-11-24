#ifndef SCENE_H
#define SCENE_H

#include <vector>
#include "Object.hpp"

namespace me
{
    class Scene
    {
        public:
            /** Default constructor */
            Scene();
            /** Default destructor */
            virtual ~Scene();

            virtual void Tick();
            void Render(sf::RenderTarget& target);
        protected:
            std::vector<Object*> m_Objects;
        private:
    };
};

#endif // SCENE_H
