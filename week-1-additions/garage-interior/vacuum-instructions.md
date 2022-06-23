I know, I know. I really need to get this `garage-floor` cleaned up.
Peeking at it now I see that it's just *covered* in junk.
The `robo-vac.py` *should* do the trick, but the thing is busted.
I don't have time to look at it right now, but I'm leaving myself a note on what to do.

The `robo-vac.py` itself is a one-foot-by-one-foot-by-one-foot cube, with a vacuum attachment fitted to the bottom.
That being the case, it can clean one square foot of a floor at any given time.
The lil' guy moves pretty slowly--this was so I could make sure it's not a hazard while I'm working in here.
It can move one foot in any cardinal direction (i.e., north, south, east, and west) in five seconds.
The garage itself is built so that each wall also faces a cardinal direction.

(I find drawing pictures of all of this helps me keep this information straight.)

Now, here's the thing: the robot's main functionality in the `main()` function is up to snuff and shouldn't need to be adjusted.
However, it's `battery_calculator()` function needs some TLC. To say the least.

This is because the `robo-vac.py` will only fire up once it's *sure* it has enough battery to get the job done.
The battery in the vacuum can take a while to charge up, but it drains at a very consistent 1% per minute.

The robot's charging station is in the NW corner of the garage.
When it fires up, the `robo-vac.py` will start moving along the north wall towards the east wall.
Once it hits the wall, it'll move one foot south before moving west towards the west wall.
Upon hitting the wall again, it moves yet another foot south, before heading east.
It continues this process indefinitely until it hits one of the southernmost corners,
when it'll make one more swipe across the width of the room
(going either east or west, depending on which wall its against when it hits one of the southernmost corners).

(Again, pictures come in handy for me when imagining the robot's pathing.)

The robot shuts down once it has completed this last pass across the width of the room.
(Unfortunately, I have to manually bring it back to its charging station, but thankfully it's pretty small.)

So here's the long and short of it: **the `battery_calculator()` function inside of the `robo-vac.py`**
**needs to be able to calculate the `percentage_battery_remaining` after cleaning a room,**
**given the `width` and `length` of that room.**

It shouldn't be too difficult to implement--I just haven't had a chance to do so yet.
Too many other exciting projects to work on!

Whenever I do get around to it though, there's one thing I'll need to keep in mind:
it might seem like if I had a small room that was two feet by two feet,
then it would take the robot 20 seconds to clean the room.
But actually, it would only take the robot 15 seconds!
That's because the second I power it on it instantly cleans the space it's inhabiting.

(If I'm confused by that idea, I might think about drawing it out...that always helps me!)

It's also important to note that the `percentage_battery_remaining` that the `battery_calculator()` function produces
should be a `float`, which is essentially **a number with a decimal point**. If there's 53% battery remaining,
then that should be represented as `0.53`.

Well, that should be enough information to get me started...whenever I get around to fixing this thing, that is.