#ifndef MOVIE_H
#define MOVIE_H

#include "Scene.hpp"

namespace me
{
    class Animation : public Scene
    {
        public:
            /** Default constructor */
            Animation();
            /** Default destructor */
            virtual ~Animation();
        protected:
        private:
    };
};

#endif // MOVIE_H
