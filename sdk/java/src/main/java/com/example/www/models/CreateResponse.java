/*
 * BouncerAPILib
 *
 * This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
 */
package com.example.www.models;

import java.util.*;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonSetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonInclude.Include;

@JsonInclude(Include.ALWAYS)
public class CreateResponse 
        implements java.io.Serializable {
    private static final long serialVersionUID = 107512445699149781L;
    private Result4 result;
    /** GETTER
     * TODO: Write general description for this method
     */
    @JsonGetter("Result")
    public Result4 getResult ( ) { 
        return this.result;
    }
    
    /** SETTER
     * TODO: Write general description for this method
     */
    @JsonSetter("Result")
    public void setResult (Result4 value) { 
        this.result = value;
    }
 
}