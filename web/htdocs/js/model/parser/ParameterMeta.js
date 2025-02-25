/**
 * Parameter metadata
 */
class ParameterMeta {

    data = null;          // Parameter metadata
    parameter = null;    // Parameter descriptor
    parser = null;
    #range = null;

    constructor(parser, meta, parameter) {
        this.data = meta || {};
        this.parameter = parameter;
        this.parser = parser;

        if (this.data.range) {
            this.#range = new ParameterRange(parser, this.data.range);
        }
    }   

    /**
     * Returns a ParameterRange object if a range exists
     */
    range() {
        return this.#range;
    }

    /**
     * If possible, returns a list of values, null if not possible.
     */
    async getValues() {
        if (this.#range) return this.#range.getValues();
        return this.data.values || null;
    }

    /**
     * Determines the default value for the parameter
     */
    getDefaultValue() {
        // If we have a parameter default, use it
        if (this.parameter.default) {
            return this.parameter.default;
        }

        // If we have a default defined in the metadata, use it
        if (this.data.default) {
            return this.data.default;
        }

        const that = this;

        function getNumberDefault() {
            if (that.data.range && that.data.range.min) {
                return "" + that.data.range.min;
            }
            return "0";
        }

        function getSelectDefault() {
            if (!that.data.values) throw new Error("No values for select type: " + that.parameter.name);

            return "" + that.data.values[0].value;
        }

        // If we have a type definition, derive the default from this
        if (this.data.type) {
            switch (this.data.type) {
                case "int": return getNumberDefault();
                case "float": return getNumberDefault();
                case "select": return getSelectDefault();
                case "bool": return "False";
                case "color": return "(0, 0, 0)";
                default: throw new Error("Unknown parameter type: " + this.data.type);
            }
        }
        
        // Last fallback: None
        return "None";
    }
}