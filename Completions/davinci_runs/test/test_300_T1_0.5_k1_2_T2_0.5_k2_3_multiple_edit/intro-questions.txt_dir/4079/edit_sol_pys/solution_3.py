#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b on 2019-05-07.
#  2019, SMART Health IT.


import os
import pytest
import io
import unittest

from .fixtures import force_bytes
from .. import task


@pytest.mark.usefixtures("base_settings")
class TaskTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Task", js["resourceType"])
        return task.Task(js)
    
    def testTask1(self):
        inst = self.instantiate_from("task-example-fetch.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask1(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask1(inst2)
    
    def implTask1(self, inst):
        self.assertEqual(force_bytes(inst.authoredOn.date), force_bytes("2016-10-31"))
        self.assertEqual(force_bytes(inst.authoredOn.as_json()), force_bytes("2016-10-31"))
        self.assertEqual(force_bytes(inst.businessStatus.coding[0].code), force_bytes("on-hold"))
        self.assertEqual(force_bytes(inst.businessStatus.coding[0].display), force_bytes("On Hold"))
        self.assertEqual(force_bytes(inst.businessStatus.coding[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/task-business-status"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Fetch patient document"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("payload"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("document"))
        self.assertEqual(force_bytes(inst.contained[2].id), force_bytes("reference"))
        self.assertEqual(force_bytes(inst.description), force_bytes("Fetch and store a document from a DocumentReference"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-fetch"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://example.org/fetchtask"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("fetchtask123"))
        self.assertEqual(force_bytes(inst.input[0].type.text), force_bytes("Patient Document Reference"))
        self.assertEqual(force_bytes(inst.input[1].type.text), force_bytes("Requested Document Class"))
        self.assertEqual(force_bytes(inst.input[2].type.text), force_bytes("Requested Document Type"))
        self.assertEqual(force_bytes(inst.input[3].type.text), force_bytes("Requested Document Profile"))
        self.assertEqual(inst.intent, "order")
        self.assertEqual(force_bytes(inst.lastModified.date), force_bytes("2016-10-31"))
        self.assertEqual(force_bytes(inst.lastModified.as_json()), force_bytes("2016-10-31"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(force_bytes(inst.meta.tag[0].display), force_bytes("test health data"))
        self.assertEqual(force_bytes(inst.meta.tag[0].system), force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"))
        self.assertEqual(force_bytes(inst.output[0].type.text), force_bytes("Fetched Document"))
        self.assertEqual(force_bytes(inst.owner.display), force_bytes("Dr. Adam Careful"))
        self.assertEqual(force_bytes(inst.owner.reference), force_bytes("Practitioner/example"))
        self.assertEqual(force_bytes(inst.performerType[0].text), force_bytes("Performer"))
        self.assertEqual(force_bytes(inst.priority), force_bytes("routine"))
        self.assertEqual(force_bytes(inst.reasonCode[0].text), force_bytes("The Task.reason should only be included if there is no Task.focus or if it differs from the reason indicated on the focus"))
        self.assertEqual(force_bytes(inst.status), force_bytes("ready"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">[Put rendering here]</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testTask2(self):
        inst = self.instantiate_from("task-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Task instance")
        self.implTask2(inst)
        
        js = inst.as_json()
        self.assertEqual("Task", js["resourceType"])
        inst2 = task.Task(js)
        self.implTask2(inst2)
    
    def implTask2(self, inst):
        self.assertEqual(force_bytes(inst.authoredOn.date), force_bytes("2015-03-10"))
        self.assertEqual(force_bytes(inst.authoredOn.as_json()), force_bytes("2015-03-10"))
        self.assertEqual(force_bytes(inst.basedOn[0].display), force_bytes("Referral from the emergency department"))
        self.assertEqual(force_bytes(inst.basedOn[0].reference), force_bytes("ServiceRequest/fm-referral"))
        self.assertEqual(force_bytes(inst.businessStatus.text), force_bytes("Specimens collected"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Specimen Collection"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("SpecimenCollection"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Specimen Collection"))
        self.assertEqual(force_bytes(inst.context.reference), force_bytes("Encounter/example"))
        self.assertEqual(force_bytes(inst.definitionReference.display), force_bytes("Specimen Collection Template"))
        self.assertEqual(force_bytes(inst.definitionReference.reference), force_bytes("http://hl7.org/fhir/Task/example"))
        self.assertEqual(force_bytes(inst
