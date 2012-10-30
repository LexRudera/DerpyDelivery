#ifndef MOVIE_H
#define MOVIE_H

#include "Scene.hpp"

namespace tg
{
    class Movie : public Scene
    {
        public:
            /** Default constructor */
            Movie();
            /** Default destructor */
            virtual ~Movie();
        protected:
        private:
    };
}

#endif // MOVIE_H
