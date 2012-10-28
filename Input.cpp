#include "Input.hpp"

// Remember this! If you wanna roll with static members, Re-declare them out here like it was a function! The
// compiler won't be able to get to the actual variable. It actually makes sense in the way, that in the header
// you make a map to the variables and functions, and in here you actually make the destination. Remember that
// this makes sense in that, when you make a new object. it makes all the variables declared in the header. The
// statics are around, not really caring if there are any objects. Who's gonna make them a place to hang out then,
// if the objects dont? You are!
//std::vector<Input*> Input::s_inputs;
// Alright, SFML doesn't support multiple input sources, so screw this.

// Well, now it's static, and basically just being an easy wrapper around SFML's own two Mouse and Keyboard classes.
// What am i gonna do with this place?
