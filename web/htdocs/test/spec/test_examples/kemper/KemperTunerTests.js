class KemperTunerTests extends KemperTestBase {

    /**
     * {
     *      switchDefinitions: Array of switch definitions
     * }
     */
    async testTriggeredFromClient(options = {}) {
        const that = this;

        function getSwitchColors() {
            const ret = [];
            for (const switchDef of options.switchDefinitions) {
                ret.push(that.runner.getSwitchColor(switchDef));
            }  
            return ret;  
        }

        function getDisplayCornerColors() {
            return [
                that.runner.getDisplayColorAt([1, 1]),
                that.runner.getDisplayColorAt([1, 238]),
                that.runner.getDisplayColorAt([238, 1]),
                that.runner.getDisplayColorAt([238, 238])
            ];
        }

        // Remember old colors
        const oldSwitchColors = getSwitchColors();
        const oldDisplayColors = getDisplayCornerColors();
            
        // Enable tuner
        this.runner.client.parameters.get(new NRPNKey([127, 126])).setValue(1);
        await this.runner.tick();

        expect(getSwitchColors()).toEqual(oldSwitchColors.map((item) => [0, 0, 0]));
        expect(getDisplayCornerColors()).toEqual(oldDisplayColors.map((item) => [0, 0, 0]));

        // Disable tuner
        this.runner.client.parameters.get(new NRPNKey([127, 126])).setValue(3);
        await this.runner.tick();

        expect(getSwitchColors()).toEqual(oldSwitchColors);
        expect(getDisplayCornerColors()).toEqual(oldDisplayColors);
    }
}