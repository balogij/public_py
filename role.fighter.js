var roleUpgrader = {

    /** @param {Creep} creep **/
    run: function(creep) {

        var enemies= creep.room.find('FIND_HOSTILE_CREEPS');

/*        
        var closestHostile = creep.pos.findClosestByRange(FIND_HOSTILE_CREEPS);
        if(creep.attack(closestHostile) == ERR_NOT_IN_RANGE)
*/

        if(enemies.length>0){
            console.log('Enemies: ' + enemies.length);
            creep.moveTo(enemies[0]);
            creep.attack(enemies[0]);
        }
        else
        {
            console.log('Enemies: ' + enemies.length);
        }
    }
};

module.exports = roleUpgrader;