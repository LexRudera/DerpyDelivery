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
            void Render();
        protected:
        private:
            std::vector<Object*> m_Objects;
    };
};

#endif // SCENE_H
